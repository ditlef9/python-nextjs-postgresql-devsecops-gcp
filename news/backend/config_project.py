# config_project.py

def config_project():
    """
    Connection type:
      * tcp_socket  - Connecting to local PostgresSQL instance running on 127.0.0.1 (on example Windows)
      * unix_socket - Connecting to Google Cloud PostgresSQL instance  (in production on Google Cloud Functions)

    DB User:
      * root - Always the same

    DB_NAME:
      * What database we want to connect to

    DB_PORT:
      * 5432 - Always the same

    DB_INSTANCE_UNIX_SOCKET:
      * /cloudsql/PROJECT:europe-north1:DATABASE_NAME - For connecting to Google Cloud PostgresSQL

    :return:
    """
    return {
        "GOOGLE_CLOUD_PROJECT_ID": "applications-dev-453706",
        "DB_CONNECTION_TYPE": "tcp_socket",
        "DB_HOST": "127.0.0.1",
        "DB_USER": "postgres",
        "DB_PASS": "root",
        "DB_NAME": "news-dev",
        "DB_PORT": "5432",
        "DB_INSTANCE_UNIX_SOCKET": "",
    }
