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
8. [🔒 Authenticate](#-8-authenticate)
9. [📄 Getting sensors](#-9-getting-sensors)
10. [📊 Creating Excel with sensors](#-10-creating-excel-with-sensors)
11. [☁️ Uploading Excel to Buckets](#%EF%B8%8F-11-uploading-excel-to-buckets)
12. [📧 Sending Excel as email](#-12-sending-excel-as-email)
13. [🖥️ Running the Report Excel-generation Locally](#%EF%B8%8F-13-running-the-report-excel-generation-locally)
14. [☁️ Running the Report Excel-generation on Google Cloud Run Functions](#%EF%B8%8F-14-running-the-report-excel-generation-on-google-cloud-run-functions)
15. [📜 License](#-15-license)

---

## 📖 1 Learning Objectives for Report Excel-generation

By the end of this module, you will learn how to:

* Connect to a REST API with Python
* Authenticate to a REST API and using Bearer token (JWT token)
* Create a spreadsheet with Python

---

## ✨ 2 Lessons Overview for Report Excel-generation


1. **Introduction**

2. **Creating Python Backend**<br>
- Implementing core functionality for Python application
- Activity/Reflection


3. **Setting up Google Cloud Infrastructure for Report PDF-generation**<br>
- Creating and configuring Google Cloud resources (Cloud Functions, Buckets, Scheduler, and Secret Manager).
- Activity/Reflection

4. **Getting a LimaCharlie organization**<br>
- Signing up at LimaCharlie and adding two sensors.
- Activity/Reflection

5. **Connecting to LimaCharlie REST API using Postman**<br>
- How to get a Bearer token
- Activity/Reflection

6. **Authenticate**<br>
- Authenticate with Python
- Activity/Reflection

7. **Getting sensors**<br>
- Listing sensors with Rest API
- Activity/Reflection

8️. **Creating Excel with sensors**<br>
- Createing a spreadsheet using Python
- Activity/Reflection

9. **Uploading Excel to Buckets**<br>
- Uploading the spreadsheet to buckets
- Activity/Reflection

10. **Sending Excel as email**<br>
- Sending spreadsheet as email to receivers using Gmail
- Activity/Reflection

11. **Congratulations and Learning Tip**<br>
- Learning tip: Apply what you learn to real-world scenarios or personal projects. Hands-on experience reinforces concepts better than passive learning.
- Reflection: How can you integrate automation into your daily workflow to improve efficiency?

12. **Quiz**


---

# 📸 3 Diagram and Screenshots from Report Excel-generation

**Report Excel Diagram**<br>
A scheduler wil start the function every month. This starts a function that will get a list of sensors, and
put it into a spreadsheet.<br>
![Report Excel-generation Diagram](_docs/report-excel-generation-diagram.drawio.png) 

**Email with Excel report**<br>
The report is sent to receivers email address with the spreadsheet as attachment.<br>
![Email with Excel report](_docs/excel-gmail.png) 

**Buckets**<br>
The spreadsheet is uploaded to Google Cloud Buckets.<br>
![Report Buckets](_docs/buckets-excel.png) 

**Limacharlie**<br>
The spreadsheet contains a list of sensors.<br>
![Limacharlie](_docs/limacharlie.png) 

**Spreadsheet**<br>
Image of spreadsheet.<br>
![Spreadsheet](_docs/spreadsheet-python.png) 

---

## 🐍 4 Creating Python Report Excel-generation


**1. Create new repository in Github**

**2. Open application in PyCharm**

Pycharm > File > Close Project<br><br>

Pycharm > Get from VCS<br><br>


**3. Add requirements.txt**

```
functions-framework         # Added by YOUR_NAME. Framework for running Google Cloud Functions locally
flask                       # Added by YOUR_NAME. Micro web framework for building web applications.
google-cloud-storage        # Added by YOUR_NAME. Interact with Google Cloud Storage for file operations.
google-cloud-secret-manager # Added by YOUR_NAME. Read and write secrets to Google Cloud
pandas                      # Added by YOUR_NAME. Library used for , data manipulation and analysis.
openpyxl                    # Added by YOUR_NAME. Required by pandas to save Excel files.
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


### Create Bucket

Google Cloud > Buckets > New

* Name: report-excel-bucket
* Labels: owner: YOUR_NAME
* Location type: Region

Add rule:
* Auto delete after 7 days.


### Publish Application

Change `applications-dev-453706` with your Google Cloud project ID.

```commandline
gcloud auth login
gcloud functions deploy report-excel --gen2 --runtime=python312 --region=europe-north1 --source=. --entry-point=main --trigger-http --timeout=540 --verbosity=info --project=applications-dev-453706 --memory=256Mi --set-env-vars=GOOGLE_CLOUD_PROJECT_ID=applications-dev-453706
```

### Add Scheduler

Google Cloud > Scheduler > Create Job

Define the schedule:

* Name: **report-excel-monthly-report**
* Region: **europe-west1 (Belgium)**
* Description: **Generates a report**
* Frequency: `0 0 1 * *` (At 00:00 on day-of-month 1.)
* Time zone: **Central European Standard Time (CET)**

Configure the execution:

* Target type: **HTTP**
* URL: **https://news-frontend-644994207224.europe-north1.run.app** (Change with your url)
* Auth header: **Add OIDC token**
* Service account: **Cloud Run Functions and Scheduler Service Account**
* Scope: **https://news-frontend-644994207224.europe-north1.run.app** (Change with your url)

[Create]

### Create secret

* Create secret `report-excel-services` (you can copy `what-version-services`)<br>
```json
{
"gmail_sender_email": "YOU@gmail.com",
"gmail_app_password": "CHANGE ME",
"recipient_email_addresses": "YOU@gmail.com",
"limacharlie_organization_id": "We will enter this later",
"limacharlie_api_key": "We will enter this later"
}
```


---

## 🧪 6 Getting a LimaCharlie organization

1. https://app.limacharlie.io
2. Create an organization
2. Copy organization from URL https://app.limacharlie.io/orgs/**b65162e2-3493-5d2f-a236-03f690dd9180** to secret `report-excel-services`
3. Access management > REST API > Create API Key
* Permissions: sensor.get and sensor.list
* Name: report-excel

4. Copy the API key into `limacharlie_api_key` to secret `report-excel-services`.

5. Sensors > Sensors List > Add Sensor
* JSON Logs > (Create a Installation key) 
* Ingest Method: Events received through LimaCharlie webhooks
* Adapter Name: Finance application
* Secret: Random Secret

6. Sensors > Sensors List > Add Sensor
* JSON Logs > (Create a Installation key) 
* Ingest Method: Events received through LimaCharlie webhooks
* Adapter Name: Firewall Alerts
* Secret: Random Secret

---

## 🔗 7 Connecting to LimaCharlie REST API using Postman

* Download and install Postman
* Open documentation: https://api.limacharlie.io/static/swagger/

1 Authenticate
  * https://app.limacharlie.io/jwt
  * headers:
    * Content-Type: application/json
  * body:
    * oid: LIMACHARLIE_ORGANIZATION_ID
    * secret: LIMACHARLIE_API_KEY

2 List sensors
  * https://api.limacharlie.io/v1/sensors/LIMACHARLIE_ORGANIZATION_ID
  * headers:
    * Content-Type: application/json
    * Authorization: Bearer ey....


---

## 🔒 8 Authenticate

* Copy src/utils/google_secret_manager_access_secret_version.py
* Implement src/limacharlie/auth_limacharlie.py

---

## 📄 9 Getting sensors

* Implement src/limacharlie/sensors_list.py


---

## 📊 10 Creating Excel with sensors

* Copy src/utils/get_datetime.py
* Implement src/spreadsheet/spreadsheet.py

---

## ☁️ 11 Uploading Excel to Buckets

* Copy src/utils/google_bucket_storage_client_and_get_bucket.py
* Copy src/utils/google_bucket_write_from_filename.py
* Implement upload in main.py

---

## 📧 12 Sending Excel as email

* Copy src/utils/send_gmail_app_pass.py
* Implement src/email/send_email.py
---

## 🖥️ 13 Running the Report Excel-generation Locally

**1. Clone the repository**


**2. Open the directory `news-backend` in PyCharm**


**3. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**4. Start the application**<br>
In PyCharm go to main.py and click `Run`


---

## ☁️ 14 Running the Report Excel-generation on Google Cloud Run Functions




---

## 📜 15 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

