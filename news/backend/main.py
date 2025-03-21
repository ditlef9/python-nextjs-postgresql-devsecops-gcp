import json
import os

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

from config_project import config_project
from src.api.news.create_news import create_news
from src.api.news.delete_news import delete_news
from src.api.news.edit_news import edit_news
from src.api.news.get_all_news import get_all_news
from src.api.news.get_single_news import get_single_news
from src.api.users.delete_user import delete_user
from src.api.users.edit_user import edit_user
from src.api.users.get_user import get_user
from src.api.users.get_users import get_users
from src.api.users.log_in import log_in
from src.api.users.register import register
from src.dao.db_adapter import DBAdapter
from src.utils.google_secret_manager_access_secret_version import google_secret_manager_access_secret_version

# - Flask App --------------------------------------------------------------
app = Flask(__name__)
#CORS(app)  # Enable CORS for all routes
CORS(app, origins=["http://localhost:3000", "https://news-frontend-644994207224.europe-north1.run.app"])

# - Secret -----------------------------------------------------------------
read_config_project_dict = config_project()  # Call the function to get the config dictionary
news_secret_services = google_secret_manager_access_secret_version(project_id=read_config_project_dict['GOOGLE_CLOUD_PROJECT_ID'], secret_id="news-services")
try:
    secret_dict = json.loads(news_secret_services)
except Exception as e:
    raise Exception(f"Error converting news_secret_services to json: {e}")
jwt_secret_key = secret_dict["jwt_secret_key"]


# - Database ---------------------------------------------------------------
db = DBAdapter(client_secret_dict=secret_dict, migrations=False, debug=True)


@app.route('/api/migrations', methods=['GET'])
def __migrations():
    print(f"__migrations() · Init")
    db.migrations()
    return {"message": f"Migrations Ok", "data": None, "error": "Success"}, 200


# - General ----------------------------------------------------------------
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(os.path.join(app.root_path, 'src/static'), 'index.html', mimetype='text/html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'src/static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon') # noqa

# - Users ---------------------------------------------------------------------
@app.route('/api/users/register', methods=['POST'])
def __register():
    return_tuple: tuple = register(db)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]


@app.route('/api/users/log-in', methods=['POST'])
def __log_in():
    print(f"__log_in() · Init")
    return_tuple: tuple = log_in(db=db, jwt_secret_key=jwt_secret_key)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]


@app.route('/api/users/get-users', methods=['GET'])
def __get_users():
    return_tuple: tuple = get_users(db=db, jwt_secret_key=jwt_secret_key)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]

@app.route('/api/users/get-user/<int:user_id>', methods=['GET'])
def __get_user(user_id):
    return_tuple: tuple = get_user(db=db, jwt_secret_key=jwt_secret_key, get_user_id=user_id)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]

@app.route('/api/users/edit-user/<int:user_id>', methods=['POST'])
def __edit_user(user_id):
    return_tuple: tuple = edit_user(db=db, jwt_secret_key=jwt_secret_key, get_user_id=user_id)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]

@app.route('/api/users/delete-user/<int:user_id>', methods=['POST'])
def __delete_user(user_id):
    return_tuple: tuple = delete_user(db=db, jwt_secret_key=jwt_secret_key, get_user_id=user_id)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]

# - News ---------------------------------------------------------------------

@app.route('/api/news/create-news', methods=['POST'])
def __create_news():
    return_tuple: tuple = create_news(db=db, jwt_secret_key=jwt_secret_key)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]


@app.route('/api/news/get-all-news', methods=['GET'])
def __get_all_news():
    return_tuple: tuple = get_all_news(db=db)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]


@app.route('/api/news/get-single-news/<int:news_id>', methods=['GET'])
def __get_single_news(news_id):
    return_tuple: tuple = get_single_news(db=db, jwt_secret_key=jwt_secret_key, get_news_id=news_id)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]


@app.route('/api/news/edit-news/<int:news_id>', methods=['POST'])
def __edit_news(news_id):
    return_tuple: tuple = edit_news(db=db, jwt_secret_key=jwt_secret_key, get_news_id=news_id)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]


@app.route('/api/news/delete-news/<int:news_id>', methods=['POST'])
def __delete_news(news_id):
    return_tuple: tuple = delete_news(db=db, jwt_secret_key=jwt_secret_key, get_news_id=news_id)
    return {"message": return_tuple[0]['message'], "data": return_tuple[0]['data'], "error": return_tuple[0]['error']}, return_tuple[1]

# - Main start ----------------------------------------------------------------
if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    # Start app
    print("main()·Flask API running in Developing Mode")
    print("main()·Login with: gcloud auth application-default login")
    print("main()·Migrations: https://localhost:8080/api/migrations")
    db.migrations()
    app.run(debug=True,
            host="0.0.0.0",
            port=8080,
            ssl_context=('src/certificates/localhost_cert.pem',
                         'src/certificates/localhost_key.pem'))
