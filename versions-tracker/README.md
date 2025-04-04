# 🔄 Versions Tracker

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

Based on a list of software this app checks if there are any new version available. 
If there is a new version then there will be sent an email to the receivers.

| Category     | Details                               |          
|--------------|---------------------------------------|
| Tech         | Python                                |
| Runs on      | Cloud Run Functions                   |
| GCP Services | Buckets, Secrets, Scheduler and Email |



Table of contents:
1. [📖 Learning Objectives for Versions Tracker](#-1-learning-objectives-for-versions-tracker)
2. [✨ Lessons Overview for Versions Tracker](#-2-lessons-overview-for-version-tracker)
3. [📸 Diagram and Screenshots from Versions Tracker](#-3-diagram-and-screenshots-from-version-tracker)
4. [🚀 Create Python Application for Versions Tracker](#-4-create-python-application-for-version-tracker)
5. [☁️ Configure Google Cloud Infrastructure](#%EF%B8%8F-5-configure-google-cloud-infrastructure)
6. [⚡ Configure CI/CD with GitHub Actions](#-6-configure-cicd-with-github-actions)
7. [🕒 Setup a Google Cloud Scheduler](#-7-setup-a-google-cloud-scheduler)
8. [💻 Implementing Check for New Versions](#-8-implementing-check-for-new-versions)
9. [✉️ Implementing Email Message if There Are New Version](#%EF%B8%8F-9-implementing-email-message-if-there-are-new-version)
10. [🖥️ Running the Finished Version Tracker Locally](#%EF%B8%8F-10-running-the-finished-versions-tracker-locally)
11. [☁️ Running the Finished Version Tracker on Google Cloud Run Functions](#%EF%B8%8F-11-running-the-finished-versions-tracker-on-google-cloud-run-functions)
12. [📜 License](#-12-license)

---

## 📖 1 Learning Objectives for Version Tracker

* Create a **Python application** with **Google Cloud Run Functions**.
* Set up **Google Cloud services** like **Buckets**, **Email**, **Secrets** and **Scheduler**.
* Automate deployment using **GitHub Actions** (CI/CD - Continuous Integration and Continuous Deployment/Delivery).
* Use **Google Cloud Scheduler** to run tasks periodically.
* Send **email notifications** for new versions.

---

## ✨ 2 Lessons Overview for Version Tracker

1. **Introduction**

2. **Create Python application**<br>
- Create a new application locally and push it to Github.<br>
- Activity: Import the project into Snyk. Are there any vulnerabilities?

3. **Configure Google Cloud Infrastructure** <br>
- Create a bucket
- Activity/Reflection: 

4. **Configure CI/CD with Github Actions**<br>
- Create a service account and Github Actions file
- Activity/Reflection: What is the difference between Cloud Run and Cloud Run Functions?

5. **Setup a scheduler**<br>
- Create a new Google Cloud Scheduler that checks for new versions
- Reflection: How often should the scheduler run?

6. **Check for New Versions from FTP**<br>
- Program the check for new versions
- Activity/Reflection: What other services do you use?

7. **Check for New Versions from releases**<br>
- Program the check for new versions
- Activity/Reflection:

8. **Implement loop in main**<br>
- In main read applications_list.json and loop over it
- Activity/Reflection: 

9. **Implement Bucket check**<br>
- In main read data from bucket, and store latest versions there
- Activity/Reflection: 

10. **Implementing Email Message if There Are New Version**<br>
- If there are any new versions we want an email
- Activity/Reflection: Is there a better way than email?

11. **Congratulations and Learning Tip**<br>
- Learning tip: As you work through each step, don’t wait until the end to test your application. 
- Reflection: What Did You Learn?

12. **Quiz**

---

## 📸 3 Diagram and Screenshots from Version Tracker

**Version Tracker Diagram**<br>
This diagram shows the structure and flow of the Version Tracker, outlining its components and how user data is processed.<br>
![Version Tracker Diagram](_docs/versions-tracker-diagram.drawio.png) 

**Email With New Versions**<br>
If there are any new versions they will be emailed to the recipients<br>
![Email with new versions](_docs/screenshots/email_with_new_versions.png) 


---

## 🚀 4 Create Python Application for Version Tracker

**1. Create new application in Github**

* Name: version-tracker-python-gcp
* Description: Based on a list of software this app checks if there are any new version available. 

**2. Open application in PyCharm**

Pycharm > File > Close Project<br><br>

Pycharm > Get from VCS<br><br>


**3. Add requirements.txt**

```
functions-framework         # Added by YOUR_NAME. Framework for running Google Cloud Functions locally
google-cloud-storage        # Added by YOUR_NAME. Interact with Google Cloud Storage for file operations
google-cloud-secret-manager # Added by YOUR_NAME. Read and write secrets to Google Cloud
flask                       # Added by YOUR_NAME. To run the application locally
beautifulsoup4              # Added by YOUR_NAME. Library that makes it easy to scrape information from web pages
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


**5. Setup venv**

Windows:
```commandline
python -m venv env
env\Scripts\activate 
```

Linux/Mac:
```commandline
python -m venv env
env/Scripts/activate 
```


**6. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**7. Run application**<br>
In PyCharm go to main.py and click `Run`


---

## ☁️ 5 Configure Google Cloud Infrastructure


1. Create bucket<br>
https://console.cloud.google.com > Buckets > [Create]<br>

* Name: versions-tracker-bucket
* Labels: owner: YOUR_NAME

Location type:
* Region - europe-north1

[Create]


---

## ⚡ 6 Configure CI/CD with GitHub Actions

Manually we can deploy a Python script as a Google Cloud Run Function using this command:

```commandline
gcloud auth login

gcloud functions deploy versions-tracker --project=YOUR_PROJECT --gen2 --runtime=python312 --region=europe-north1 --source=. --entry-point=main --trigger-http --timeout=540 --max-instances=1 --verbosity=info --memory=512MB
```

**1. Enable Cloud Resource Manager API**

API and Services > Cloud Resource Manager API
https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com

**2. Create IAM Service account for Github Actions Auth**

IAM > Service accounts > + Create Service Account

* Name: **GitHub Actions Auth**
* Description: **Logs into GCP from Github in order to create new Google Cloud Run Functions**

Permissions/Assign Roles:
* Cloud Functions Admin (`roles/cloudfunctions.admin`)
* Service Account User (`roles/iam.serviceAccountUser`)
* Storage Admin (`roles/storage.admin`) (if your function uses Cloud Storage)
* Cloud Build Editor (`roles/cloudbuild.builds.editor`) (for deploying Cloud Functions)
* Viewer (`cloudfunctions.functions.get` permission)

**3. Create a key**

Service account > Keys > New

Copy the value and put it in Github > Repo > Settings > Secrets and variables > Actions > Repository secrets as 
`GCP_CREDENTIALS`.

**4. Create .github workflow**

Create a new file:<br>
`.github/workflows/google_functions_deployment.yaml`

```commandline
# Service accounts are located here:
# https://console.cloud.google.com/iam-admin/serviceaccounts
#
# This deployment uses the following service account:
# - Name: Github Actions Auth
#   ID: github-actions-auth@GOOGLE_CLOUD_PROJECT_ID.iam.gserviceaccount.com
#
# The secret is stored under 
# Github > Repo > Settings > Secrets and variables > Actions > Repository secrets as 
# `GCP_CREDENTIALS`.


name: build-and-deployment

on:
  push:
    branches:
      - main

jobs:
  deploy-production:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: 'actions/checkout@v3'
    - run: ls
    - id: 'auth'
      name: 'Authenticate to Google Cloud'
      uses: 'google-github-actions/auth@v1'
      with:
        credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

    - name: Debug GCP credentials
      env:
        GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GCP_CREDENTIALS }}
      run: |
        echo "$GOOGLE_APPLICATION_CREDENTIALS" > credentials.json

    - name: 'Set up Cloud SDK'
      uses: 'google-github-actions/setup-gcloud@v1'
      with:
        version: '>= 363.0.0'
    - name: 'Use gcloud CLI'
      run: 'gcloud info' 
    - name: Install Python dependencies
      run: |
        pip install -r requirements.txt
    - name: 'Deploy a gen 2 cloud function'
      run: 'gcloud functions deploy version-tracker --project=YOUR_PROJECT --gen2 --runtime=python312 --region=europe-north1 --trigger-http --source=. --entry-point=main --max-instances=1 --memory=256MB --timeout=60s'



```


---


## 🕒 7 Setup a Google Cloud Scheduler



https://console.cloud.google.com > Cloud Scheduler > [Create Job]<br>

**Define the schedule**<br>
* Name: versions-tracker-scheduler
* Region: europe-west1 (Belgium)
* Descriptions: Triggers the Version Tracker function to check if there are any new versions.
* Frequency: 0 9 1 */3 *
* Timezone: Central European Standard Time (CET)

**Configure the execution**<br>
* Target Type: HTTP
* URL: URL_TO_FUNCTION
* HTTP method: GET
* Auth header: Add OIDC Token
* Service account: Cloud Run, Cloud Run Functions and Scheduler Service Account
* Scope: URL_TO_FUNCTION

[Create]



---

## 💻 8 Implementing Check for New Versions


1. Implement applications_list.json

2. Implement get_version_list.py

3. Implement get_version_github.py 

4. Implement loop in main

5. Add Bucket to main


---

## ✉️ 9 Implementing Email Message if There Are New Version

1. Create a secret `versions-tracker-services`:

Google Cloud > Secret manager > New

* Name: **versions-tracker-services**
* Secret value: 
```json
{
"gmail_sender_email": "YOU@gmail.com",
"gmail_app_password": "APP_PASSWORD",
"recipient_email_addresses":   "YOU@gmail.com"
}
```
* Location(s): **europe-north1**
* Labels: 
  * owner: YOUR_NAME
  * app: versions-tracker

2. Implement send_gmail_app_pass.py

3. Implement send_email.py <br>
Change the project ID.

4. On new version send email


---

## 🖥️ 10 Running the Finished Version Tracker Locally

**1. Clone the repository**

**2. Open the directory `versions-tracker` in PyCharm**


**3. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`

**4. Start the application**<br>
In PyCharm go to main.py and click `Run`



---

## ☁️ 11 Running the Finished Versions Tracker on Google Cloud Run Functions

### 1. Create service account `Cloud Scheduler Service Account for Cloud Run and Functions` (one time setup)

IAM > Service accounts > + Create Service Account

* Name: **Cloud Scheduler Service Account for Cloud Run and Functions**
* Description: **This is used for Google Cloud Scheduler. It can read secrets and invoke functions**

Permissions/Assign Roles:
* Cloud Scheduler Service Agent
* Service Account Admin


### 2. Create bucket

**Create Bucket:**

Buckets > [Create]

Get started:
* Name: **versions-tracker-bucket**
* Labels: owner: YOUR_NAME

Location type:
* Region - europe-north1

[Create]


### 3. Deploy on Cloud Run Functions

```commandline
gcloud auth login
gcloud functions deploy versions-tracker --gen2 --runtime=python312 --region=europe-north1 --source=. --entry-point=main --trigger-http --timeout=540 --verbosity=info --project=applications-dev --memory=512MB
```



---

## 📜 12 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

