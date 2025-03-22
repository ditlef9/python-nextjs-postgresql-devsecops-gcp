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



Table of contents:
1. [📖 Learning Objectives for Report Excel-generation](#-1-learning-objectives-for-report-excel-generation)
2. [✨ Lessons Overview for Report Excel-generation](#-2-lessons-overview-for-report-excel-generation)
3. [📸 Diagram and Screenshots from Report Excel-generation](#-3-diagram-and-screenshots-from-report-excel-generation)
4. [🐍 Creating Python Report Excel-generation](#-4-creating-python-report-excel-generation)
5. [🌐 Setting up Google Cloud Infrastructure for Report Excel-generation](#-5-setting-up-google-cloud-infrastructure-for-report-excel-generation)
6. [🧪 Getting a LimaCharlie organization](#-6-getting-a-limacharlie-organizationw)
7. [🔗 Connecting to LimaCharlie REST API using Postman](#-7-connecting-to-limacharlie-rest-api-using-postman)
8. [📄 Getting sensors](#-8-getting-sensors)
9. [📊 Creating Excel with sensors](#-9-creating-excel-with-sensors)
10. [☁️ Uploading Excel to Buckets](#%EF%B8%8F-10-uploading-excel-to-buckets)
11. [📧 Sending Excel as email](#-11-sending-excel-as-email)
12. [🖥️ Running the Report Excel-generation Locally](#%EF%B8%8F-12-running-the-report-excel-generation-locally)
13. [☁️ Running the Report Excel-generation on Google Cloud Run Functions](#%EF%B8%8F-13-running-the-report-excel-generation-on-google-cloud-run-functions)
14. [📜 License](#-14-license)

---

## 📖 1 Learning Objectives for Report Excel-generation

By the end of this module, you will learn how to:

---

## ✨ 2 Lessons Overview for Report Excel-generation


---

# 📸 3 Diagram and Screenshots from Report Excel-generation

**Report Excel Diagram**<br>
A scheduler wil start the function every month. This starts a function that will get a list of sensors, and
put it into a spreadsheet.<br>
![Report Excel-generation Diagram](_docs/report-excel-generation-diagram.drawio.png) 

---

## 🐍 4 Creating Python Report Excel-generation


**1. Create new repository in Github**

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
    print("report-excel-generation local run")

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

## 🌐 5 Setting up Google Cloud Infrastructure for Report Excel-generation

---

## 🧪 6 Getting a LimaCharlie organization

---

## 🔗 7 Connecting to LimaCharlie REST API using Postman

---

## 📄 8 Getting sensors

---

## 📊 9 Creating Excel with sensors

---

## ☁️ 10 Uploading Excel to Buckets


---

## 📧 11 Sending Excel as email

---

## 🖥️ 12 Running the Report Excel-generation Locally

**1. Clone the repository**


**2. Open the directory `news-backend` in PyCharm**


**3. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**4. Start the application**<br>
In PyCharm go to main.py and click `Run`


---

## ☁️ 13 Running the Report Excel-generation on Google Cloud Run Functions




---

## 📜 14 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

