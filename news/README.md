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


# ![News Backend and Frontend Diagram](_docs/news-diagram.drawio.png) 

Table of contents:
1. [🚀 Getting Started with News Backend and Frontend](#-1-getting-started-with-user-feedback-form)
2. [📦 Python Utils and Functions](#-2-nextjs-utils-and-functions)
3. [📦 Next.js Utils and Functions](#-2-nextjs-utils-and-functions)
4. [🖥️ Running the Finished News Backend and Frontend Locally](#%EF%B8%8F-3-running-the-finished-user-feedback-form-locally)
5. [☁️ Running the Finished News Backend and Frontend on Google Cloud Run](#%EF%B8%8F-4-running-the-finished-user-feedback-form-on-google-cloud-run)
6. [📜 License](#-5-license)

---

## 🚀 1 Getting Started with News Backend and Frontend



### 1.1 Backend


**1. Create new application in Github**

**2. Open application in PyCharm**

Pycharm > File > Close Project<br><br>

Pycharm > Get from VCS<br><br>


**3. Add requirements.txt**

```
functions-framework         # Added by YOUR_NAME. Framework for running Google Cloud Functions locally.
google-cloud-storage        # Added by YOUR_NAME. Interact with Google Cloud Storage for file operations.
```

**4. Create main.py**

```python


import flask
import functions_framework

@functions_framework.http
def main(request: flask.wrappers.Request):
    """HTTP Cloud Function"""
    log_headline: str = f"main()"
    print(f"{log_headline} · Init")


if __name__ == '__main__':
    print("what-version local run")

    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)
```

**5. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**6. Run application**<br>
In PyCharm go to main.py and click `Run`


### 1.2 Frontend


---

## 📦🐍 2 Python Utils and Functions


---

## 📦🌐 3 Next.js Utils and Functions



---

## 🖥️ 4 Running the Finished News Backend and Frontend Locally

**1. Clone the repository**

### 4.1 Backend

**1. Open the directory `news-backend` in PyCharm**


**2. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**3. Start the application**<br>
In PyCharm go to main.py and click `Run`


### 4.2 Frontend


---

## ☁️ 5 Running the Finished News Backend and Frontend on Google Cloud Run

### 5.1. Create service account `Cloud Scheduler Service Account for Cloud Run and Functions` (one time setup)

IAM > Service accounts > + Create Service Account

* Name: **Cloud Scheduler Service Account for Cloud Run and Functions**
* Description: **This is used for Google Cloud Scheduler. It can read secrets and invoke functions**

Permissions/Assign Roles:
* Cloud Scheduler Service Agent
* Service Account Admin


### 5.2. Database

**Create Bucket:**

Buckets > [Create]

Get started:
* Name: **what-version-bucket**
* Labels: owner: YOUR_NAME

Location type:
* Region - europe-north1

[Create]


### 5.3. Deploy News Backend on Google Cloud Run

### 5.4. Deploy News Frontend on Google Cloud Run




---

## 📜 6 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

