# 📊 Report Excel-generation

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

Generates Excel reports from stored data.

| Category     | Details        |          
|--------------|----------------|
| Tech         | Python (Flask) |
| Runs on      | Cloud Run      |
| GCP Services | Buckets        |


# ![Report Excel-generation Diagram](_docs/report-excel-generation-diagram.drawio.png) 

Table of contents:
1. [🚀 Getting Started with Report Excel-generation](#-1-getting-started-with-report-excel-generation)
2. [📦 Python Utils and Functions](#-2-python-utils-and-functions)
3. [🖥️ Running the Report Excel-generation Locally](#%EF%B8%8F-3-running-the-finished-report-excel-generation-locally)
4. [☁️ Running the Report Excel-generation on Google Cloud Run](#%EF%B8%8F-4-running-the-finished-report-excel-generation-on-google-cloud-run)
5. [📜 License](#-5-license)

---

## 🚀 1 Getting Started with Report Excel-generation




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
    print("versions-tracker local run")

    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)
```

**5. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**6. Run application**<br>
In PyCharm go to main.py and click `Run`



---

## 📦 2 Python Utils and Functions




---

## 🖥️ 3 Running the Finished Report Excel-generation Locally

**1. Clone the repository**


**2. Open the directory `news-backend` in PyCharm**


**3. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**4. Start the application**<br>
In PyCharm go to main.py and click `Run`




---

## ☁️ 4 Running the Finished Report Excel-generation on Google Cloud Run

### 4.1. Create service account `Cloud Scheduler Service Account for Cloud Run and Functions` (one time setup)

IAM > Service accounts > + Create Service Account

* Name: **Cloud Scheduler Service Account for Cloud Run and Functions**
* Description: **This is used for Google Cloud Scheduler. It can read secrets and invoke functions**

Permissions/Assign Roles:
* Cloud Scheduler Service Agent
* Service Account Admin


### 4.2. Bucket

**Create Bucket:**

Buckets > [Create]

Get started:
* Name: **what-version-bucket**
* Labels: owner: YOUR_NAME

Location type:
* Region - europe-north1

[Create]


### 4.3. Deploy on Google Cloud Run




---

## 📜 5 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

