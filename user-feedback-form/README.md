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


# ![User Feedback Form Diagram](_docs/user-feedback-form-diagram.drawio.png) 

Table of contents:
1. [✨ Lessons Overview](#-1-lessons-overview)
2. [🚀 Getting Started with User Feedback Form](#-2-getting-started-with-user-feedback-form)
3. [☁️ Running User Feedback Form on Google Cloud Run](#%EF%B8%8F-3-running-user-feedback-form-on-google-cloud-run)
4. [📦 Next.js Utils and Functions](#-4-nextjs-utils-and-functions)
5. [🖥️ Running the User Feedback Form Locally](#%EF%B8%8F-5-running-user-feedback-form-locally)
6. [🛡️ Add Application to Snyk](#%EF%B8%8F-6-add-application-to-snyk)
7. [📜 License](#-7-license)

---

## ✨ 1 Lessons Overview

1. **Introduction**

2. **Creating app** - Create a new application locally and push it to Github.

3. **Setup GCP Infrastructure** - Setup a GCP project, service account, bucket and the Cloud Run application.

4. **DevSecOps Integration** - Integrate Github repository with Snyk

5. **Creating the Form and Styling it** - First create the form, then add CSS, then we will add const for the form, feedback, 
   handle form input change and submit

6. **Bucket Integration** - We will build the api that handles form submit which has a bucket integration

7. **Email Integration** - Add email notification when someone sends the form

8. **Congratulations and Learning Tip**

---


## 🚀 2 Getting Started with User Feedback Form

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


## ☁️ 3 Running User Feedback Form on Google Cloud Run

### 3.1 Create a Google Cloud Console Project (one time setup)

https://console.cloud.google.com/ > https://console.cloud.google.com/projectcreate

* Name: applications-dev


### 3.2 Create service account to lunch applications (one time setup)

IAM > Service accounts > + Create Service Account

* Name: **Cloud Run, Cloud Run Functions and Scheduler Service Account**
* Description: **This is used for Cloud Run, Cloud Run Functions and Scheduler Service. It can read secrets and invoke Run and Functions**

Permissions/Assign Roles:
* Cloud Scheduler Service Agent
* Service Account Admin


### 3.3 Create bucket

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

### 3.4 Make sure that the application has a Docker file

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

### 3.5 Deploy on Cloud Run

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

## 📦 4 Next.js Utils and Functions

Send email: 
[https://github.com/sendgrid/sendgrid-nodejs/tree/main/packages/mail](https://github.com/sendgrid/sendgrid-nodejs/tree/main/packages/mail)


---

## 🖥️ 5 Running the Finished User Feedback Form Locally

**1. Clone the repository**

**2. Open the directory `user-feedback-form` in VSCode**

**3. Start the application**

```
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the application.



---


## 🛡️ 6 Add Application to Snyk


---

## 📜 7 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

