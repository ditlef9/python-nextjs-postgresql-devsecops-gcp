# 📄 Report PDF-generation

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

Generates PDF reports from stored data.

| Category     | Details          |          
|--------------|------------------|
| Tech         | Python (Flask)   |
| Runs on      | Cloud Run        |
| GCP Services | Secrets, Buckets |



Table of contents:
1. [📖 Learning Objectives for Report PDF-generation](#-1-learning-objectives-for-news-backend-and-frontend)
2. [✨ Lessons Overview for Report PDF-generation](#-2-lessons-overview-for-news-backend-and-frontend)
3. [📸 Diagram and Screenshots from Report PDF-generation](#-3-diagram-and-screenshots-from-versions-tracker)
4. [🖨️ Install Weasyprint](#-4-creating-python-backend)
5. [🐍 Creating Python Report PDF-generation](#-4-creating-python-backend)
6. [🌐 Setting up Google Cloud Infrastructure for Report PDF-generation](#-6-setting-up-google-cloud-infrastructure-for-new-backend-and-frontend)
7. [🧪 Generating test data: Assets and their vulnerabilities (critical, high, medium, low)](#)
8. [📄 Creating PDF](#)
9. [📄 Creating PDF with Vulnerabilities](#)
10. [📊 Adding a barchart](#)
11. [☁️ Uploading PDF to Buckets](#)
12. [📧 Sending PDF as email](#)
13. [🖥️ Running the Report PDF-generation Locally](#%EF%B8%8F-3-running-the-finished-report-pdf-generation-locally)
14. [☁️ Running the Report PDF-generation on Google Cloud Run](#%EF%B8%8F-4-running-the-finished-report-pdf-generation-on-google-cloud-run)
15. [📜 License](#-5-license)

---

## 📖 1 Learning Objectives for Report PDF-generation

* ..
* ..
* ..
* ..

---

## ✨ 2 Lessons Overview for Report PDF-generation

1. **Introduction**

2. **Creating Python Backend**<br>
- 
- Activity/Reflection

---

## 📸 3 Diagram and Screenshots from Report PDF-generation


**Report PDF-generation Diagram**<br>
This diagram shows the structure and flow, outlining its components and how user data is processed.<br>
![Report PDF-generation Diagram](_docs/report-pdf-generation-diagram.drawio.png) 


---

## 🐍 4 Creating Python Report PDF-generation


**1. Create new repository in Github**

**2. Open application in PyCharm**

Pycharm > File > Close Project<br><br>

Pycharm > Get from VCS<br><br>


**3. Add requirements.txt**

```
flask                       # Added by YOUR_NAME. Micro web framework for building web applications.
flask-cors                  # Added by YOUR_NAME. Enables Cross-Origin Resource Sharing (CORS) in Flask apps.
google-cloud-storage        # Added by YOUR_NAME. Interact with Google Cloud Storage for file operations.
matplotlib                  # Added by YOUR_NAME. Plotting and data visualization library.
numpy                       # Added by YOUR_NAME. Library for numerical computation.
reportlab                  # Added by YOUR_NAME. Generation of PDF.

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
    print("report-pdf local run")

    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)
```

**5. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**6. Set environment variable and Run application**<br>

PyCharm > Edit Configurations > Python

* Name: **main**
* Script: **main.py**
* Environment variables: PYTHONUNBUFFERED=1;**GOOGLE_CLOUD_PROJECT_ID=applications-dev-453706**


In PyCharm click `Run`



---

## 🌐 5 Setting up Google Cloud Infrastructure for Report PDF-generation

### Create Bucket

Google Cloud > Buckets > New

* Name: report-pdf-bucket
* Labels: owner: YOUR_NAME
* Location type: Region

Add rule:
* Auto delete after 7 days.


### Publish Application

```commandline
gcloud auth login
gcloud functions deploy report-pdf --gen2 --runtime=python312 --region=europe-north1 --source=. --entry-point=main --trigger-http --timeout=540 --verbosity=info --project=applications-dev-453706 --memory=256Mi
```

### Add Scheduler

Google Cloud > Scheduler > Create Job

Define the schedule:

* Name: **report-pdf-monthly-report**
* Region: **europe-west1 (Belgium)**
* Description: **Generates a report**
* Frequency: **0 0 1 * *** (At 00:00 on day-of-month 1.)
* Time zone: Central European Standard Time (CET)

Configure the execution:

* Target type: **HTTP**
* URL: **https://news-frontend-644994207224.europe-north1.run.app** (Change with your url)
* Auth header: **Add OIDC token**
* Service account: **Cloud Run Functions and Scheduler Service Account**
* Scope: **https://news-frontend-644994207224.europe-north1.run.app** (Change with your url)

[Create]

---

## 🧪 6 Generating test data: Assets and their vulnerabilities (critical, high, medium, low)

** Implement `src/test_data/generate_test_data.py`


---

## 📄 7 Creating PDF

** Implement `src/application/a_delete_old/a_delete_old.py`
** Implement `src/application/b_create_tmp/b_create_tmp.py`
** Implement `src/application/c_generate_pdf/c_generate_pdf.py`
** Implement `src/application/x_save_pdf/x_save_pdf.py`

---

## 📄 8 Creating PDF with Vulnerabilities

** Add ```
    # Load bucket
    bucket = google_bucket_storage_client_and_get_bucket(bucket_name="report-pdf-bucket")```
** Implement `src/application/e_assets/e_assets.py`
** Implement `src/application/e_assets/helpers/load_assets.py`

---

## 📊 9 Adding a barchart

** Implement `src/utils/d_graph_severity/d_graph_severity.py`
** Implement `src/utils/d_assets.py/helpers/graphs/draw_bar_chart.py`


---


## ☁️ 9 Uploading PDF to Buckets

** Implement `src/application/y_upload_to_bucket/y_upload_to_bucket.py`

---

## 📧 10 Sending PDF as email

---



## 🖥️ 11 Running the Report PDF-generation Locally

**1. Clone the repository**


**2. Open the directory `news-backend` in PyCharm**


**3. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**4. Start the application**<br>
In PyCharm go to main.py and click `Run`




---

## ☁️ 12 Running the Report PDF-generation on Google Cloud Run

### 12.1. Create service account `Cloud Scheduler Service Account for Cloud Run and Functions` (one time setup)

IAM > Service accounts > + Create Service Account

* Name: **Cloud Scheduler Service Account for Cloud Run and Functions**
* Description: **This is used for Google Cloud Scheduler. It can read secrets and invoke functions**

Permissions/Assign Roles:
* Cloud Scheduler Service Agent
* Service Account Admin


### 12.2. Bucket

**Create Bucket:**

Buckets > [Create]

Get started:
* Name: **what-version-bucket**
* Labels: owner: YOUR_NAME

Location type:
* Region - europe-north1

[Create]


### 13.3. Deploy on Google Cloud Run




---

## 📜 13 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

