# 📝 News Backend and Frontend

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

Backend API with user authentication and Next.js frontend.

| Category     | Details                 |          
|--------------|-------------------------|
| Tech         | Python (Flask), Next.js |
| Runs on      | Cloud Run               |
| GCP Services | PostgreSQL              |



Table of contents:
1. [📖 Learning Objectives for News backend and Frontend](#-1-learning-objectives-for-news-backend-and-frontend)
2. [✨ Lessons Overview for News backend and Frontend](#-2-lessons-overview-for-news-backend-and-frontend)
3. [📸 Diagram and Screenshots from News backend and Frontend](#-3-diagram-and-screenshots-from-versions-tracker)
4. [🐍 Creating Python Backend](#-4-creating-python-backend)
5. [⚛️ Creating Next.js Frontend](#%EF%B8%8F-5-creating-nextjs-frontend)
6. [🌐 Setting up Google Cloud Infrastructure for New backend and Frontend](#-6-setting-up-google-cloud-infrastructure-for-new-backend-and-frontend)
7. [🔗 Connecting to Database with pgAdmin](#-7-connecting-to-database-with-pgadmin)
8. [🛢️ Python DBAdapter](#%EF%B8%8F-8-python-dbadapter)
9. [📝 Register](#-9-register)
10. [🔑 Login](#-10-login)
11. [📰 Create news](#-11-create-news)
12. [📃 List news](#-12-list-news)
13. [✏️ Edit news](#%EF%B8%8F-13-edit-news)
14. [🗑️ Delete news](#%EF%B8%8F-14-delete-news)
15. [🖥️ Running the Finished News Backend and Frontend Locally](#%EF%B8%8F-15-running-the-finished-news-backend-and-frontend-locally)
16. [☁️ Running the Finished News Backend and Frontend on Google Cloud Run](#%EF%B8%8F-16-running-the-finished-news-backend-and-frontend-on-google-cloud-run)
17. [📜 License](#-17-license)

---

## 📖 1 Learning Objectives for News backend and Frontend

* Build a **Flask-based backend**  with user authentication and a PostgreSQL database.
* Develop a **Next.js frontend** to interact with the backend API.
* Deploy the application on Google Cloud using **Cloud Run** and **PostgreSQL**.
* **Secure APIs** and authentication with best practices.


---

## ✨ 2 Lessons Overview for News backend and Frontend


1. **Introduction**

2. **Creating Python Backend**<br>
- Setting up a Flask-based backend and structuring the project.
- Activity/Reflection: What challenges did you face while setting up the backend?


3. **Creating Next.js Frontend**<br>
- Setting up a Next.js project and creating the UI components.
- Activity/Reflection: How does the frontend connect with the backend?


4. **Setting up Google Cloud Infrastructure for New backend and Frontend**<br>
- Configuring Cloud Run, PostgreSQL, and Secret Manager.
- Activity/Reflection: What are the key advantages of deploying on Google Cloud?

5. **Connecting to database**<br>
- Establishing a secure connection between your computer and and PostgreSQL.
- Activity/Reflection: Why is database security important in production?


6. **Python DBAdapter**<br>
- Establishing a secure connection between Flask and PostgreSQL.
- Activity/Reflection: How can database abstraction improve maintainability?


7. **Register**<br>
- Implementing user registration with validation and password hashing.
- Activity/Reflection: What security measures should be in place for user registration?

8. **Login**<br>
- Authenticating users and managing sessions/tokens.
- Activity/Reflection: What authentication method did you choose and why?

9. **Create news**<br>
- Creating an API to add news articles with authentication.
- Activity/Reflection: What data validation checks are necessary for posting news?

10. **List news**<br>
- Implementing an API to fetch and display news articles.
- Activity/Reflection: How does pagination improve user experience?

11. **Edit news**<br>
- Allowing authorized users to update existing news articles.
- Activity/Reflection: How do you handle permissions for editing content?

12. **Delete news**<br>
- Implementing secure deletion of news articles.
- Activity/Reflection: What precautions should be taken when deleting records?

13. **Congratulations and Learning Tip**<br>
- Learning tip: ?
- Reflection: ?

14. **Quiz**

---

## 📸 3 Diagram and Screenshots from News backend and Frontend

**News Backend and Frontend Diagram**<br>
This diagram shows the structure and flow of the Version Tracker, outlining its components and how user data is processed.<br>
![News Backend and Frontend Diagram](_docs/news-diagram.drawio.png) 


---

## 🐍 4 Creating Python Backend


**1. Create new application in Github**

* Name: news-backend-python


**2. Open application in PyCharm**

Pycharm > File > Close Project<br><br>

Pycharm > Get from VCS<br><br>


**3. Create certificates**

Windows:
```
# Create the directories
mkdir src
mkdir src\certificates

# Change to the certificates directory
cd src\certificates

# Generate the SSL certificate using OpenSSL
openssl req -x509 -newkey rsa:4096 -keyout localhost_key.pem -out localhost_cert.pem -sha256 -days 365 -nodes -subj "/C=NO/ST=Oslo/L=Oslo/O=My Company/CN=example.com/emailAddress=admin@example.com"


```

Ubuntu:
```
mkdir src
mkdir src/certificates
cd src/certificates
openssl req -x509 -newkey rsa:4096 -keyout localhost_key.pem -out localhost_cert.pem -sha256 -days 365 -nodes -subj "/C=NO/ST=Oslo/L=Oslo/O=My Company/CN=example.com/emailAddress=admin@example.com"
```

**4. Add Dockerfile**<br>

```
# Specify Python
FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Open port
EXPOSE 8080

# Add Python script
RUN mkdir /app
WORKDIR /app
COPY . .


# Install dependencies
RUN pip install -r requirements.txt

# Set Pythons path
ENV PYTHONPATH /app

# Run script
CMD [ "python", "./src/main.py" ]

```

**5. Create a index.html file**<br>

`src/static/index.html`

```html
<!DOCTYPE html>
<html lang="en-US">
<head>
    <title>It works</title>
    <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
    <style>
    /*- Body -------------------------------------------------------------------------- */
    html, body, div, span, object, iframe, img {
        margin:0;
        padding:0;
        border:0;
        outline:0;
        background:transparent;
    }
    html,body {
        margin:0;
        padding:0;
    }
    body {
        background: #f8f8f8;
        color: #000;
        font: normal 16px Helvetica, Arial, sans-serif, 'Open Sans';
    }
    /*- Headlines ----------------------------------------------------------------------- */
    h1{
        color: #272727;
        font: bold 21px Helvetica, Arial, sans-serif, 'Open Sans';

    }
    /*- Paragraph ----------------------------------------------------------------------- */
    p{
        color: #000000;
        font: normal 16px Helvetica, Arial, sans-serif, 'Open Sans';
    }
    /*- Main -------------------------------------------------------------------------- */
    main {
        background: #ffffff;
        border-radius: 25px;
        padding: 20px;
        margin: 0px auto;
        margin-top: 20px;
        margin-bottom: 20px;
        text-align: center;
        width: 500px;
    }
    @media screen and (max-width: 52.375em) {
        main{
            width: 90%;
        }
    }
    </style>
</head>
<body>


<main>
    <h1>It works</h1>
    <p>Welcome to the application</p>
</main>

</body>
</html>
```

**6. Create a favicon.ico file**<br>

Download favicon and add it to the `static` directory:

[favicon.ico](_docs/favicon.ico)

**7. Add requirements.txt**

```
flask                     # Added by YOUR_NAME. Added by YOUR_NAME.A lightweight WSGI web application framework.
flask-cors                # Added by YOUR_NAME. CORS (Cross-Origin Resource Sharing) support for Flask.
pg8000                    # Added by YOUR_NAME. A Pure Python database driver for PostgreSQL.
google-cloud-secret-manager # Added by YOUR_NAME. Google Cloud Secret Manager client library for Python.
sqlalchemy                # Added by YOUR_NAME. SQLAlchemy ORM and database toolkit for Python.

```

**8. Create src/main.py**

```python
import os

from flask import Flask, send_from_directory
from flask_cors import CORS
from pathlib import Path

# - Flask App -------------------------------------------------------------------
app = Flask(__name__)

# - Set up CORS to allow only the frontend domain in production -----------------
frontend_url = "https://my-frontend-service.a.run.app"
cors = CORS(app, resources={r"/*": {"origins": frontend_url}})
app.config['CORS_HEADERS'] = 'Content-Type'


# - General ----------------------------------------------------------------
@app.route('/', methods=['GET'])
def __index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html', mimetype='text/html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon') # noqa



# - Main start ----------------------------------------------------------------
if __name__ == "__main__":

    # Developing or production?
    home = str(Path.home())
    home_array = home.split("\\")
    if home_array[0] in ["C:" "/Users/YOUR_MAC_OR_UBUNTU_USERNAME"]:
        # Run Database Migrations
        # db.run_migrations()

        # Developing mode
        print("main()·Flask API running in Developing Mode")

        # Start app
        app.run(debug=True, 
                host="0.0.0.0",
                port=8080,
                ssl_context=('src/certificates/localhost_cert.pem',
                             'src/certificates/localhost_key.pem'))

    else:
        # Production mode
        print("main()·Flask API running in Production Mode")

        # Start app
        app.run(debug=False, host="0.0.0.0", port=8080)
```

**9. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`



**10. Run application**<br>
In PyCharm go to main.py and click `Run`



---

## ⚛️ 5 Creating Next.js Frontend



**1. Create new repository in Github**

*Name: **news-frontend-nextjs**

**2. Create new application**

Open CMD/Terminal and write:

```
mkdir next
cd next
npx create-next-app@latest
```

* What is your project name: **news**
* Would you like to use TypeScript: **Yes**
* Would you like to use ESLint: **Yes**
* Would you like to use Tailwind CSS: **No**
* Would you like yor code inside a `src/` directory: **No**
* Would you like to use App Router? (recommended): **Yes**
* Would you like to use Turbopack for `next dev`?: **No**
* Would you like to customize the import alias (`@/*` by default)?: **No**

**3. Initialize files to Github**

File > Terminal:

```
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_REPOSITORY_NAME.git
git push -u origin main
```


**4. Add Dockerfile**

Add `Dockerfile` in the project with the following contents:

```
FROM node:alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```


**5. Start the application**

```
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the application.

---

## 🌐 6 Setting up Google Cloud Infrastructure for New backend and Frontend

### 6.1 Create PostgresSQL database

https://console.cloud.google.com > SQL > [Create Instance]<br>

* Choose your database engine: **PosgtreSQL**
* Choose a Cloud SQL edition: Enterprise
* Edition preset: Sandbox

**Instance info**<br>
* Database version: Latest
* Instance ID: news-postgres-prod
* Password: random password (https://my.norton.com/extspa/passwordmanager?path=pwd-gen)


**Choose region and zonal availability**<br>
* Region: europe-north1 (Finland)
* Zonal Availability: Single zone

**Machine configuration**<br>
* Machine shapes: Shared core
* 1 vCPI, 0.614 GB

**Storage**<br>
* Storage type: HDD
* Storage capacity: 10 GB

**Data protection**<br>
* Automated daily backups: Uncheck

**Labels**<br>
* owner = YOUR_NAME


### 6.3 Create secret

https://console.cloud.google.com > Secret Manager > + Create Secret

* Name: news-services
* Secret value:
```commandline
{
    "DB_CONNECTION_TYPE": "unix_socket",
    "DB_HOST": "127.0.0.1",
    "DB_USER": "news-postgres-prod",
    "DB_PASS": "YOUR_SQL_PASSWORD",
    "DB_NAME": "postgres",
    "DB_PORT": "5432",
    "DB_INSTANCE_UNIX_SOCKET": "/cloudsql/GCP_PROJECT_ID:europe-north1:news-postgres-prod",
}
```

* Replication policy Locations: **europe-north1**
* Labels:
  * owner = YOUR_NAME
  * app = news


### 6.4 Deploy backend
Cloud Run > Deploy Container > Service

Configure:
* Service name: news-backend
* Region: europe-north1 (Finland)
* Authentication: Allow unauthenticated invocations
* Billing: Request based

Service Scaling
* Auto-scaling: Checked
* Minimum number of instances: 0

Containers > Resources:
* Memory: 128 MB

Containers > Revision scaling:
* Minimum number of instances: 0
* Maximum number of instances: 1

Containers > Security:
* Service account: Cloud Run, Cloud Run Functions and Scheduler Service Account
* 

### 6.5 Deploy frontend

Cloud Run > Deploy Container > Service

Configure:
* Service name: news-frontend
* Region: europe-north1 (Finland)
* Authentication: Allow unauthenticated invocations
* Billing: Request based

Service Scaling
* Auto-scaling: Checked
* Minimum number of instances: 0

Containers > Resources:
* Memory: 128 MB

Containers > Revision scaling:
* Minimum number of instances: 0
* Maximum number of instances: 1

Containers > Security:
* Service account: Cloud Run, Cloud Run Functions and Scheduler Service Account

---

## 🔗 7 Connecting to Database with pgAdmin

---

## 🛢️ 8 Python DBAdapter

---

## 📝 9 Register


---

## 🔑 10 Login

---

## 📰 11 Create news

---

## 📃 12 List news

---

## ✏️ 13 Edit news

---

## 🗑️ 14 Delete news

---

## 🖥️ 15 Running the Finished News Backend and Frontend Locally


---

## ☁️ 16 Running the Finished News Backend and Frontend on Google Cloud Run

---

## 📜 17 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

