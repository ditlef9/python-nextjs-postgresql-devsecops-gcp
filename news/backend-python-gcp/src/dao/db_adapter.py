import datetime
import os
import ssl
from pathlib import Path

import sqlalchemy


from google.cloud.sql.connector import IPTypes, Connector
import pg8000

from config_project import config_project


class DBAdapter:
    """
    Handles database calls to PostgresSQL.
    The database connection string is located in config_project.py
    Works with SQLAlchemy version 2 and newer
    """
    # Pool
    __pool = None

    # Misc
    __debug: bool = None
    __prod_or_dev: str = None
    __config: dict = None

    # Database connection
    __db_connection_type: str = None
    __db_host: str = None
    __db_user: str = None
    __db_pass: str = None
    __db_name: str = None
    __db_port: str = None
    __prefix: str = "n"
    __db_instance_unix_socket: str = None

    def __init__(self, client_secret_dict: dict, debug: bool = False, migrations: bool = False):
        # Debug
        self.__debug = debug
        if debug:
            print("DBAdapter()·Init with debug mode enabled")

        # Find if we are in production or development
        self.prod_or_dev()

        # Read config
        self.read_db_config(client_secret_dict=client_secret_dict)

        # Create connection pool
        self.__pool = self.init_connection_pool()

        # Run migration
        if migrations:
            self.migrations()

    # - Prod or dev ------------------------------------------------------------------------------------
    def prod_or_dev(self):
        # Are we running locally or in production?
        home_pathlib = Path.home().resolve()
        home_str: str = str(home_pathlib)

        # Test production first
        if home_str == "/www-data-home" or home_str == "/home" or home_str == "/home/cnb":
            if self.__debug:
                print(f"DBAdapter()·prod_or_dev()·We are in Prod because home_str={home_str}")
            self.__prod_or_dev = "prod"
            self.__slack_channel = "production"
            return ""

        # Test Windows
        windows = home_str.split("\\")
        if windows[0] == "C:":
            if self.__debug:
                print(f"DBAdapter()·prod_or_dev()·We are in Windows dev because we got and C: in home_str={home_str}")
            self.__prod_or_dev = "dev"
            self.__slack_channel = "development"
            return ""

        # Test Ubuntu and Mac
        dev_dirs = [Path("/Users/")]
        if home_pathlib.parent in dev_dirs:
            if self.__debug:
                print(f"DBAdapter()·prod_or_dev()·We are in Ubuntu/Mac dev because home_str={home_str} is a part of dev_dirs")
            self.__prod_or_dev = "dev"
            self.__slack_channel = "development"
            return ""

        # Fallback is prod
        if self.__debug:
            print(f"DBAdapter()·prod_or_dev()·We are unsure if we are in prod or dev, so we use fallback prod. home_str={home_str}")
        self.__prod_or_dev = "prod"
        self.__slack_channel = "production"
        return ""

    # - Read config -----------------------------------------------------------------------------------
    def read_db_config(self, client_secret_dict: dict):
        """
        Reads config and sets it as class variables
        """

        # Read connection config
        read_config_project_dict = config_project()  # Call the function to get the config dictionary


        # Try environment variables
        if 'DB_USER' in os.environ:
            self.__db_connection_type = "connector"
            self.__db_instance_connection_name = os.environ["DB_INSTANCE_CONNECTION_NAME"]
            self.__db_user = os.environ['DB_USER']
            self.__db_pass = os.environ['DB_PASS']
            self.__db_name = os.environ['DB_NAME']
        else:
            if self.__prod_or_dev == "dev":

                self.__db_connection_type = read_config_project_dict['DB_CONNECTION_TYPE']
                self.__db_host = read_config_project_dict['DB_HOST']
                self.__db_user = read_config_project_dict['DB_USER']
                self.__db_pass = read_config_project_dict['DB_PASS']
                self.__db_name = read_config_project_dict['DB_NAME']
                self.__db_port = read_config_project_dict['DB_PORT']
                if self.__debug:
                    print(f"DBAdapter()·read_db_config()·Dev environment with connection type {self.__db_connection_type}")
            else:
                # client_secret = google_secret_manager_access_secret_version(project_id=read_config_project_dict['GOOGLE_CLOUD_PROJECT_ID'], secret_id="news-services")
                #c lient_secret_dict = json.loads(client_secret)
                self.__db_connection_type = client_secret_dict['DB_CONNECTION_TYPE']
                self.__db_host = client_secret_dict["DB_HOST"]
                self.__db_user = client_secret_dict["DB_USER"]
                self.__db_pass = client_secret_dict["DB_PASS"]
                self.__db_name = client_secret_dict["DB_NAME"]
                self.__db_port = client_secret_dict["DB_PORT"]
                self.__db_unix_socket_path = client_secret_dict["DB_INSTANCE_UNIX_SOCKET"]


    # - Init Connection Pool -----------------------------------------------------------------------------
    def init_connection_pool(self) -> sqlalchemy.engine.base.Engine:

        # Connect :: TCP Socket
        if self.__db_connection_type == "tcp_socket":
            if self.__debug:
                print(f"DBAdapter()·connect()·Connecting with tcp_socket to {self.__db_host}")
            return self.connect_tcp_socket(db_host=self.__db_host, db_user=self.__db_user,
                                           db_pass=self.__db_pass, db_name=self.__db_name,
                                           db_port=self.__db_port)

        # Connect :: Unix Socket (e.g. /cloudsql/project:region:instance) is defined
        if self.__db_connection_type == "unix_socket":
            if self.__debug:
                print(f"DBAdapter()·connect()·Connecting with unix_socket to {self.__db_unix_socket_path}")
            return self.connect_unix_socket(db_user=self.__db_user, db_pass=self.__db_pass, db_name=self.__db_name,
                                            db_unix_socket_path=self.__db_unix_socket_path)

        # Connect :: Connector
        if self.__db_connection_type == "connector":
            if self.__debug:
                print(f"DBAdapter()·connect()·Connecting with connector to {self.__db_instance_connection_name}")
            return self.connect_connector(db_instance_connection_name=self.__db_instance_connection_name,
                                          db_user=self.__db_user, db_pass=self.__db_pass, db_name=self.__db_name)

        # No connector
        raise ValueError(f"DBAdapter()·connect()·Missing database connection type. Please define db_connection_type which is {self.__db_connection_type}") # noqa

    # - Connect TCP Socket -----------------------------------------------------------------------------
    def connect_tcp_socket(self, db_host, db_user, db_pass, db_name, db_port) -> sqlalchemy.engine.base.Engine:
        """ Initializes a TCP connection pool for a Cloud SQL instance of Postgres. """

        connect_args = {}

        # For deployments that connect directly to a Cloud SQL instance without
        # using the Cloud SQL Proxy, configuring SSL certificates will ensure the
        # connection is encrypted.
        if os.environ.get("DB_ROOT_CERT"):
            db_root_cert = os.environ["DB_ROOT_CERT"]  # e.g. '/path/to/my/server-ca.pem'
            db_cert = os.environ["DB_CERT"]  # e.g. '/path/to/my/client-cert.pem'
            db_key = os.environ["DB_KEY"]  # e.g. '/path/to/my/client-key.pem'

            ssl_context = ssl.SSLContext()
            ssl_context.verify_mode = ssl.CERT_REQUIRED
            ssl_context.load_verify_locations(db_root_cert)
            ssl_context.load_cert_chain(db_cert, db_key)
            connect_args["ssl_context"] = ssl_context

        # [START cloud_sql_postgres_sqlalchemy_connect_tcp]
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                host=db_host,
                port=db_port,
                database=db_name,
            ),
            # [END cloud_sql_postgres_sqlalchemy_connect_tcp]
            connect_args=connect_args,
            # [START cloud_sql_postgres_sqlalchemy_connect_tcp]
            # [START_EXCLUDE]
            # [START cloud_sql_postgres_sqlalchemy_limit]
            # Pool size is the maximum number of permanent connections to keep.
            pool_size=5,
            # Temporarily exceeds the set pool_size if no connections are available.
            max_overflow=2,
            # The total number of concurrent connections for your application will be
            # a total of pool_size and max_overflow.
            # [END cloud_sql_postgres_sqlalchemy_limit]

            # [START cloud_sql_postgres_sqlalchemy_backoff]
            # SQLAlchemy automatically uses delays between failed connection attempts,
            # but provides no arguments for configuration.
            # [END cloud_sql_postgres_sqlalchemy_backoff]

            # [START cloud_sql_postgres_sqlalchemy_timeout]
            # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
            # new connection from the pool. After the specified amount of time, an
            # exception will be thrown.
            pool_timeout=30,  # 30 seconds
            # [END cloud_sql_postgres_sqlalchemy_timeout]

            # [START cloud_sql_postgres_sqlalchemy_lifetime]
            # 'pool_recycle' is the maximum number of seconds a connection can persist.
            # Connections that live longer than the specified amount of time will be
            # re-established
            pool_recycle=1800,  # 30 minutes
            # [END cloud_sql_postgres_sqlalchemy_lifetime]
            # [END_EXCLUDE]
        )
        if self.__debug:
            print("DBAdapter()·connect_tcp_socket()·Pool OK with tcp_socket")
        return pool

    # - Connect Unix Socket -------------------------------------------------------------------------------
    def connect_unix_socket(self, db_user, db_pass, db_name, db_unix_socket_path) -> sqlalchemy.engine.base.Engine:

        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
            #                         ?unix_sock=<INSTANCE_UNIX_SOCKET>/.s.PGSQL.5432
            # Note: Some drivers require the `unix_sock` query parameter to use a different key.
            # For example, 'psycopg2' uses the path set to `host` in order to connect successfully.
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_sock": "{}/.s.PGSQL.5432".format(db_unix_socket_path)},
            ),
            # [START_EXCLUDE]
            # Pool size is the maximum number of permanent connections to keep.
            pool_size=5,

            # Temporarily exceeds the set pool_size if no connections are available.
            max_overflow=2,

            # The total number of concurrent connections for your application will be
            # a total of pool_size and max_overflow.

            # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
            # new connection from the pool. After the specified amount of time, an
            # exception will be thrown.
            pool_timeout=30,  # 30 seconds

            # 'pool_recycle' is the maximum number of seconds a connection can persist.
            # Connections that live longer than the specified amount of time will be
            # re-established
            pool_recycle=1800,  # 30 minutes
            # [END_EXCLUDE]
        )

        if self.__debug:
            print("DBAdapter()·connect_tcp_socket()·Pool OK with unix_socket")
        return pool

    # - Connect Connector -------------------------------------------------------------------------------
    def connect_connector(self, db_instance_connection_name, db_user, db_pass, db_name) -> sqlalchemy.engine.base.Engine:
        """
        Initializes a connection pool for a Cloud SQL instance of MySQL.

        Uses the Cloud SQL Python Connector package.
        """
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
        ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

        connector = Connector(ip_type)

        def getconn() -> pg8000.dbapi.Connection:
            conn: pg8000.dbapi.Connection = connector.connect(
                self.__db_instance_connection_name,
                "pg8000",
                user=self.__db_user,
                password=self.__db_pass,
                db=self.__db_name,
                ip_type=ip_type,
            )
            return conn

        # The Cloud SQL Python Connector can be used with SQLAlchemy
        # using the 'creator' argument to 'create_engine'
        pool = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=getconn,
            # [START_EXCLUDE]
            # Pool size is the maximum number of permanent connections to keep.
            pool_size=5,

            # Temporarily exceeds the set pool_size if no connections are available.
            max_overflow=2,

            # The total number of concurrent connections for your application will be
            # a total of pool_size and max_overflow.

            # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
            # new connection from the pool. After the specified amount of time, an
            # exception will be thrown.
            pool_timeout=30,  # 30 seconds

            # 'pool_recycle' is the maximum number of seconds a connection can persist.
            # Connections that live longer than the specified amount of time will be
            # re-established
            pool_recycle=1800,  # 30 minutes
            # [END_EXCLUDE]
        )

        if self.__debug:
            print("DBAdapter()·connect_connector()·Pool OK with connector")
        return pool

    # - Get prefix ------------------------------------------------------------------------------------
    def get_prefix(self):
        return self.__prefix

    # - Create Liquid Base ----------------------------------------------------------------------------
    def create_migration_table(self):
        if self.__debug:
            print("DBAdapter()·connect_connector()·Creating migration table")

        # Check that liquidbase table exists
        with self.__pool.connect() as conn:
            conn.execute(sqlalchemy.text(f"""CREATE TABLE IF NOT EXISTS n_migrations (
                    base_id SERIAL PRIMARY KEY,
                    base_module VARCHAR(255),
                    base_name VARCHAR(255) NOT NULL,
                    base_run_timestamp TIMESTAMP
                )"""))
            conn.commit()

    # - Run liquid base ------------------------------------------------------------------------------
    def migrations(self):
        # Make sure migrations table exists
        self.create_migration_table()

        # Check that migrations directory exist
        if not os.path.exists(f"src/migrations"):
            os.makedirs("src/migrations", exist_ok=True)

        # Find all SQL files in liquid_base directory
        sql_files_list: list = []
        for main in os.listdir(f"src/migrations"):

            if main != "__init__.py" and main != "__pycache__":
                if os.path.isdir(f"src/migrations/{main}"):
                    for sub in os.listdir(f"src/migrations/{main}"):
                        if sub != "__init__.py" and sub != "__pycache__" and not os.path.isdir(f"src/migrations/{main}/{sub}"):
                            # print(f"DBAdapter :: setup() :: main={main} sub={sub}")
                            sql_files_list.append({"module": main, "name": sub, "full_path": f"src/migrations/{main}/{sub}"})
                else:
                    sql_files_list.append({"module": "", "name": main, "full_path": f"src/migrations/{main}"})

        # Loop through all SQL files
        for sql_file_dict in sql_files_list:
            module = sql_file_dict['module']
            name = sql_file_dict['name']
            full_path = sql_file_dict['full_path']

            # Table name
            sql_file_array = os.path.splitext(name)
            extension = sql_file_array[1].replace(".", "")
            table_name = sql_file_array[0]
            for i in range(10):
                table_name = table_name.replace(str(i), '')
            last_char = table_name[-1]
            if last_char == "_":
                table_name = table_name[: -1]

            # Check if exists in LiquidBase
            query = "SELECT * FROM n_migrations WHERE base_module=:base_module AND base_name=:base_name" # noqa
            parameters = {"base_module": module, "base_name": name}
            stmt = sqlalchemy.text(query)
            results: list = []
            try:
                # Using a with statement ensures that the connection is always released
                # back into the pool at the end of statement (even if an error occurs)
                with self.__pool.connect() as conn:
                    results = conn.execute(stmt, parameters=parameters).fetchall()
            except Exception as e:
                print(f"DBAdapter()·run_migrations()·{e} for query={query} and parameters={parameters}")
            results_len: int = len(results)
            if results_len == 0:
                # Insert
                print(f"DBAdapter()·run_migrations()·module={module} name={name} table_name={table_name} extension={extension} full_path={full_path}")  # noqa

                # Read SQL statement
                f = open(f"{full_path}", "r", encoding='UTF-8')
                sql_statement = f.read()
                f.close()

                # Replace %prefix% with real prefix
                sql_statement = sql_statement.replace("%prefix%", self.__prefix)

                # Run this sql statement
                if extension == "sql":
                    print(f"DBAdapter()·run_migrations()·Starting sql {full_path}")
                    with self.__pool.connect() as conn:
                        conn.execute(sqlalchemy.text(sql_statement))
                        conn.commit()
                elif extension == "py":
                    print(f"DBAdapter()·run_migrations()·Starting py script {full_path}")
                    if os.path.exists(full_path):
                        exec(open(full_path, encoding="UTF-8").read())
                    else:
                        exec(open("src/" + full_path).read())
                    print(f"DBAdapter()·run_migrations()·Finished with py script {full_path}")

                # Datetime
                now: datetime = datetime.datetime.now()
                datetime_ymdhms = now.strftime("%Y-%m-%d %H:%M:%S")

                # Mark it as run in liquid-base
                query: str = f"INSERT INTO n_migrations (base_module, base_name, base_run_timestamp) VALUES (:base_module, :base_name, :base_run_timestamp)"  # noqa
                parameters: dict = {"base_module": module, "base_name": name, "base_run_timestamp": datetime_ymdhms}
                self.insert(query=query, parameters=parameters)

        if self.__debug:
            print("DBAdapter()·run_migrations()·Finished")

    # - Raw Query ----------------------------------------------------------------------------------------
    def raw_query(self, query: str):
        """
        Executes a query
        :param query: DROP TABLE IF EXISTS priorities
        :return: Nothing
        """
        try:
            # Check that liquidbase table exists
            with self.__pool.connect() as conn:
                conn.execute(sqlalchemy.text(query))
                conn.commit()

                return 1
        except Exception as e:
            print(f"DBAdapter()·raw_query()·Error e={e}")
            return -1

    # - Insert --------------------------------------------------------------------------------------------
    def insert(self, query: str, parameters: dict):
        """

        :param db:
        :param query: INSERT INTO -TABLE- (time_cast, candidate) VALUES (:time_cast, :candidate)
        :param parameters: {"time_cast": time_cast, "candidate": team}
        :return:
        """
        log_headline = "DBAdapter()·insert()"

        # Insert
        stmt = sqlalchemy.text(query)
        try:
            # Using a with statement ensures that the connection is always released
            # back into the pool at the end of statement (even if an error occurs)
            with self.__pool.connect() as conn:
                conn.execute(stmt, parameters=parameters)
                conn.commit()
            # print(f"{log_headline} OK inserted data ")
        except Exception as e:
            # If something goes wrong, handle the error in this section. This might
            # involve retrying or adjusting parameters depending on the situation.
            print(f"{log_headline} · Error {e}")



    # - Select ----------------------------------------------------------------------------------------
    def select(self, query: str) -> list:
        """
        :param query: SELECT * FROM users
        :return: list of tuple with row OR NoneType if no data
        """

        try:
            with self.__pool.connect() as conn:
                # Execute the query and fetch all results
                result: list = conn.execute(sqlalchemy.text(query)).fetchall()
                return result
        except Exception as e:
            print(f"DBAdapter()·select() · Error e={e}")
            return []

    # - Select where --------------------------------------------------------------------------------------
    def select_where(self, query: str, parameters: dict):
        """
        :param query: SELECT * FROM users WHERE email=:email
        :param parameters: {"email": "sindre@cdcadvania.com"}
        :return: list of tuple with row OR NoneType if no data
        """
        log_headline = "DBAdapter()·select_where()"
        #print(f"{log_headline} query={query} parameters={parameters}")
        stmt = sqlalchemy.text(query)

        try:
            with self.__pool.connect() as conn:
                # Execute the query and fetch all results
                result = conn.execute(stmt, parameters=parameters)
                result_fetchall = result.fetchall()
                return result_fetchall

        except Exception as e:
            print(f"{log_headline} · Error e={e}")
            return []

    # - Count from rows ----------------------------------------------------------------------------------------
    def count_rows(self, rows):
        """
        :param rows:
        :return: list of tuple with row OR NoneType if no data
        """

        # Unix socket
        rows_type = type(rows)
        if rows_type == list:
            return len(rows)
        else:
            return rows.rowcount

    # - Update ---------------------------------------------------------------------------------------------------
    def update(self, query: str, parameters: dict):
        """
        :param query = '''UPDATE users_index SET
                        user_deleted_flag=:user_deleted_flag,
                        user_deleted_timestamp=:user_deleted_timestamp,
                        user_deleted_by_user_email=:user_deleted_by_user_email
                        WHERE user_id=:user_id'''
        :param parameters: {"user_deleted_flag": "1", "user_deleted_timestamp": "2023-01-01",
                            "user_deleted_by_user_email": "sindre@cdcadvania.com", "user_id": 9}
        :return: list of tuple with row OR NoneType if no data
        """
        stmt = sqlalchemy.text(query)
        try:
            with self.__pool.connect() as conn:
                conn.execute(stmt, parameters=parameters)
                conn.commit()
                print(f"DBAdapter()·update() · OK")
                return 1
        except Exception as e:
            print(f"DBAdapter()·update() · Error e={e}")
            return -1

    # - Delete ---------------------------------------------------------------------------------------------------
    def delete(self, query: str, parameters: dict):
        """
        query = '''DELETE FROM users_index WHERE user_id=:user_id'''
        parameters = { "user_id": 1 }
        """
        log_headline = "DBAdapter()·delete()"

        stmt = sqlalchemy.text(query)
        try:
            # Using a with statement ensures that the connection is always released
            # back into the pool at the end of statement (even if an error occurs)
            with self.__pool.connect() as conn:
                conn.execute(stmt, parameters=parameters)
                conn.commit()
            return 1
        except Exception as e:
            # If something goes wrong, handle the error in this section. This might
            # involve retrying or adjusting parameters depending on the situation.
            # [START_EXCLUDE]
            print(f"{log_headline} · {e}")

            return -1
