# 📊 Report Excel-generation

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

Generates Excel reports from stored data.

| Category     | Details                            |          
|--------------|------------------------------------|
| Tech         | Python, Rest API                   |
| Runs on      | Cloud Run Functions                |
| GCP Services | Buckets, Scheduler, Secrets, Email |


# ![Report Excel-generation Diagram](_docs/report-excel-generation-diagram.drawio.png) 

Table of contents:
1. [📖 Learning Objectives for Report Excel-generation](#-1-learning-objectives-for-report-pdf-generation)
2. [✨ Lessons Overview for Report Excel-generation](#-2-lessons-overview-for-report-pdf-generation)
3. [📸 Diagram and Screenshots from Report Excel-generation](#-3-diagram-and-screenshots-from-report-pdf-generation)
4. [🐍 Creating Python Report Excel-generation](#-4-creating-python-report-pdf-generation)
5. [🌐 Setting up Google Cloud Infrastructure for Report Excel-generation](#-5-setting-up-google-cloud-infrastructure-for-report-pdf-generation)
6. [🧪 Getting a LimaCharlie organization](#-6-generating-test-data-assets-and-their-vulnerabilities-critical-high-medium-low)
7. [🧪 Connecting to LimaCharlie REST API using Postman](#-6-generating-test-data-assets-and-their-vulnerabilities-critical-high-medium-low)
8. [📄 Getting sensors](#-7-creating-pdf)
9. [📄 Creating Excel with sensors](#-8-creating-pdf-with-vulnerabilities)
10. [☁️ Uploading Excel to Buckets](#%EF%B8%8F-9-uploading-pdf-to-buckets)
11. [📧 Sending Excel as email](#-10-sending-pdf-as-email)
12. [🖥️ Running the Report Excel-generation Locally](#%EF%B8%8F-11-running-the-report-pdf-generation-locally)
13. [☁️ Running the Report Excel-generation on Google Cloud Run Functions](#%EF%B8%8F-12-running-the-report-pdf-generation-on-google-cloud-run)
14. [📜 License](#-14-license)

---

## 📖 1 Learning Objectives for Report Excel-generation

By the end of this module, you will learn how to:



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

