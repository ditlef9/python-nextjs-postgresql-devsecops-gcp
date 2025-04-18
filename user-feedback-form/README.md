# 📝 User Feedback Form 

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

The user feedback form is a Next.js application that runs on Google Cloud Run.
It allows users to give their feedback and the results are stored in Google Cloud Bucket.

| Category     | Details   |          
|--------------|-----------|
| Tech         | Next.js   |
| Runs on      | Cloud Run |
| GCP Services | Buckets   |

Table of contents:
1. [📖 Learning objectives](#-1-learning-objectives)
2. [✨ Lessons Overview](#-2-lessons-overview)
3. [📸 Diagram and Screenshots from User Feedback Form](#-3-diagram-and-screenshots-from-user-feedback-form)
4. [🚀 Getting Started with User Feedback Form](#-4-getting-started-with-user-feedback-form)
5. [☁️ Running User Feedback Form on Google Cloud Run](#%EF%B8%8F-5-running-user-feedback-form-on-google-cloud-run)
6. [🛡️ Add Application to Snyk](#%EF%B8%8F-6-add-application-to-snyk)
7. [🖊️ Creating the Form Frontend](#%EF%B8%8F-7-creating-the-form-frontend)
8. [⚖️ Creating the Form Consts](#%EF%B8%8F-8-creating-the-form-consts)
9. [✏️ Creating the Form API](#%EF%B8%8F-9-creating-the-form-api)
10. [🎨 Styling the form](#-10-styling-the-form)
11. [🪣  Implementing Bucket](#-11-implementing-bucket)
12. [✉️ Implementing Email](#%EF%B8%8F-12-implementing-email)
13. [🔐 Security Command Center](#-13-security-command-center)
14. [⭐ Stars](#-9-security-command-center)
15. [📦 Next.js Utils and Functions](#-10-nextjs-utils-and-functions)
16. [🖥️ Running the User Feedback Form Locally](#%EF%B8%8F-11-running-user-feedback-form-locally)
17. [📜 License](#-12-license)

---

## 📖 1 Learning objectives

By the end of this module, you will:<br>
- Understand how to **create a Next.js application** from scratch.
- Learn to **deploy** a Next.js app on **Google Cloud Run** as a Docker container.
- Set up **Google Cloud infrastructure** including buckets and service accounts.
- Integrate **DevSecOps** tools like **Snyk** for security.
- Build a user feedback form with **form handling, validation, and storage**.
- Implement **email notifications** for submitted feedback.
- Run the application locally and **troubleshoot common issues**.

---

## ✨ 2 Lessons Overview



1. **Introduction**

2. **Creating app**<br>
- Create a new application locally and push it to Github.<br>
- Activity: Record a short summary (bullet points or voice memo) explaining the steps you followed to set up and push the app. What was the most challenging part?<br>

3. **Setup GCP Infrastructure** <br>
- Setup a GCP project, service account, bucket and the Cloud Run application.<br>
- Activity: Draw a simple diagram showing how these components interact.

4. **DevSecOps Integration** <br>
- Integrate Github repository with Snyk.<br>
- Reflection: What are the benefits and drawbacks of using 'latest' in dependencies?

5. **Creating the Form**<br>
- First, create the form<br>
- Activity: Implement Company (optional) field. 

6. **Creating the Form Consts**<br>
- Add constants for the form, feedback, handle input changes, and submit.<br>
- Activity: Implement Company (optional) field. 

7. **Creating the Form API**
- Implement API backend.<br>
- Activity: Implement Company (optional) field. 

8. **Styling the form**<br>
- Add CSS to the form.<br>
- Activity: Add icons to feedback boxes and reflect on how they improve user experience.

9. **Bucket Integration**<br>
- Build the API that handles form submission with bucket integration.<br>
- Reflection: What are some security risks when integrating with cloud storage, and how can they be mitigated?

10. **Email Integration**<br>
- Add email notification when someone submits the form.<br>
- Activity: Implement email notifications and consider how to prevent spam abuse.

11. **Security Command Center**<br>
- Demo securing our Google Cloud Environment.<br>
- Activity: Identify one security risk in your GCP setup using Security Command Center and find a way to mitigate it.

12. **Stars**<br>
- We add stars instead of drop down box.<br>
- Activity: 

13. **Congratulations and Learning Tip**<br>
-  Reflection: How do spam bots exploit web forms, and what steps can be taken to prevent them?

14. **Quiz**


---

## 📸 3 Diagram and Screenshots from User Feedback Form

**User Feedback Form Diagram**<br>
This diagram shows the structure and flow of the User Feedback Form, outlining its components and how user data is processed.<br>
# ![User Feedback Form Diagram](_docs/user-feedback-form-diagram.drawio.png) 

**User Feedback Form Filled In**<br>
This screenshot displays the User Feedback Form with filled-in data, showing how users input their responses before submitting.<br>
# ![User Feedback Form Filled in](_docs/screenshots/user-feedback-form-filled-in.png) 


**User Feedback Form Send Email to Gmail**<br>
After submission, the form sends an email with the user's feedback to a specified Gmail account for review.<br>
# ![User Feedback Form Send email to Gmail](_docs/screenshots/gmail.png) 


**All Submissions Are Stored in Google Bucket**<br>
All user submissions are stored in a Google Cloud Storage Bucket, ensuring secure and organized storage.<br>
# ![All submissions are stored in Google Bucket](_docs/screenshots/bucket-overview.png) 

**Google Bucket Single**<br>
This shows an individual submission stored in the Google Cloud Bucket, displaying the feedback data for easy retrieval.<br>
# ![Google Bucket Single](_docs/screenshots/bucket-view-single.png) 

---

## 🚀 4 Getting Started with User Feedback Form

**1. Create new repository in Github**

https://github.com/new

**2. Create new application**

Open CMD/Terminal and write:

```
mkdir next
cd next
npx create-next-app@latest
```

* What is your project name: **user-feedback-form**
* Would you like to use TypeScript: **Yes**
* Would you like to use ESLint: **Yes**
* Would you like to use Tailwind CSS: **No**
* Would you like yor code inside a `src/` directory: **No**
* Would you like to use App Router? (recommended): **Yes**
* Would you like to use Turbopack for `next dev`?: **No**
* Would you like to customize the import alias (`@/*` by default)?: **No**


**3. Open project in VSCode**

You may want to edit the workbench label format:<br>
File > Preferences > Settings > <br>
```"workbench.editor.labelFormat": "short"```

**4. Initialize files to Github**

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

**5. Start the application**

```
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the application.

---


## ☁️ 5 Running User Feedback Form on Google Cloud Run

### 5.1 Create a Google Cloud Console Project (one time setup)

https://console.cloud.google.com/ > https://console.cloud.google.com/projectcreate

* Name: applications-dev


### 5.2 Create service account to lunch applications (one time setup)


IAM > Service accounts > + Create Service Account

* Name: **Cloud Run, Cloud Run Functions and Scheduler Service Account**
* Description: **This is used for Cloud Run, Cloud Run Functions and Scheduler Service. It can read secrets and invoke Run and Functions**

Permissions/Assign Roles:
* Service Account User
* Logs Bucket Writer
* Cloud Run Admin
* Cloud Run Builder
* Secret Manager Secret Accessor
* Storage Bucket Viewer
* Storage Object Admin

For scheduler, we also need /Assign Roles:
* Cloud Run Service Invoker
* Cloud Functions Invoker

For SQL, we also need the Permissions/Assign Roles:
* Cloud SQL Client


### 5.3 Create bucket

**Create Bucket:**

Buckets > [Create]

Get started:
* Name: **user-feedback-form-bucket**
* Labels: owner: YOUR_NAME

Location type:
* Region - europe-north1

[Create]

**Change the Lifecycle:**

Lifecycle > Add a rule

Action:
* Delete object

Select object conditions:
* Age 365 days

### 5.4 Make sure that the application has a Docker file

Create a file `Dockerfile` in the project with the following contents:

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

### 5.5 Deploy on Cloud Run

Cloud Run > Deploy Container > Service

* Github - Continuously deploy from a repository (source or function)

Configure:
* Service name: user-feedback-form
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

## 🛡️ 6 Add Application to Snyk


Go to [Snyk](https://snyk.io) and import the Githu repo.

---
## 🖊️ 7 Creating the Form Frontend

* Update app/page.tsx

---

## ⚖️ 8 Creating the Form Consts

* Update app/page.tsx

---

## ✏️ 9 Creating the Form API

* Implement app/api/api-submit-form/route.ts

---


## 🎨 10 Styling the form

* Update app/globals.css


---

## 🪣 11 Implementing Bucket

1. Create an API endpoint (/app/api/api-submit-form/route.ts): This will be the main entry point that processes the form submission.

2. Create separate utility functions for uploading to Google Cloud (and sending the email later).

Folder structure:
<pre>
/app
  /api
    /api-submit-form
      route.ts      // Main API endpoint
  /utils
    uploadToGoogleBucket.ts  // Utility function for uploading to Google Cloud
    sendEmail.ts             // Utility function for sending an email
</pre>

3. Start by adding dependency to Google Cloud Storage:

```commandline
npm install @google-cloud/storage
```

4. Implement app/utils/uploadToGoogleBucket.ts

5. Implement app/api/api-submit-form/route.ts

6. When running locally remember to authenticate with
`gcloud auth application-default login`

---

## ✉️ 12 Implementing Email

1. Install Depedencies

```commandline
npm install nodemailer
npm i --save-dev @types/nodemailer
npm install dotenv
```

2. Implement app/utils/sendEmail.ts

3. Implement app/api/api-submit-form/route.ts


4. Create an app password

* Enable Two-Factor Authentication (2FA):
  - If you haven’t already enabled 2-Step Verification on your Google account, you’ll need to do so. 
  - Go to your Google Account and enable 2-Step Verification.

* Generate the App Password:
  - Once 2FA is enabled, go to the [App Passwords](https://myaccount.google.com/apppasswords) page on Google.
  - Select "Mail" as the app and "Other (Custom name)" for the device, and enter a custom name like "NodeMailer".
  - Click Generate.
  - Google will generate a 16-character password that will look something like this: abcd efgh ijkl mnop.

* Use the App Password in Your Code:
  - In your .env file, replace the SMTP_PASS value with the App Password you just generated.

5. Create a environment file

Create a file `.env.development`.<br>
Copy the file contents of `.env.example` and change all variables.<br>

6. Add the environment variables to Google Cloud Run

---

## 🔐 13 Security Command Center

Google Cloud's **Security Command Center** (SCC) helps detect threats and vulnerabilities in your cloud setup.

Key Features:
- Identifies security risks and misconfigurations.
- Monitors threats in real time.
- Provides security best practice recommendations.

Setup:
- Enable SCC in Google Cloud Console.
- Review security findings for risks.
- Take action on security alerts to protect resources.

---

## ⭐ 14 Stars

---

## 📦 15 Next.js Utils and Functions


[sendEmail](https://github.com/ditlef9/python-nextjs-postgresql-devsecops-gcp/blob/main/user-feedback-form/utils/sendEmail.ts)
Handles email notifications for feedback submissions using Nodemailer.

[uploadToGoogleBucket](https://github.com/ditlef9/python-nextjs-postgresql-devsecops-gcp/blob/main/user-feedback-form/utils/uploadToGoogleBucket.ts)
Uploads feedback to Google Cloud Storage, ensuring secure data handling.

---

## 🖥️ 16 Running the Finished User Feedback Form Locally

**1. Clone the repository**

**2. Open the directory `user-feedback-form` in VSCode**

**3. Start the application**

```
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the application.




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

