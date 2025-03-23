# 🗒️ Uptime App

[🏠 Home](../)
&nbsp; &nbsp;
[⬅ 🎯 Projects Included](../#-4-projects-included)

Tracks and manages other applications uptime.

| Category     | Details                                  |          
|--------------|------------------------------------------|
| Tech         | Next.js                                  |
| Runs on      | Cloud Run                                |
| GCP Services | PostgreSQL, Email, Secrets and Scheduler |




Table of contents:
1. [📖 Learning Objectives for Uptime App](#-1-learning-objectives-for-report-excel-generation)
2. [✨ Lessons Overview for Uptime App](#-2-lessons-overview-for-report-excel-generation)
3. [📸 Diagram and Screenshots from Uptime App](#-3-diagram-and-screenshots-from-report-excel-generation)
4. [⚛️ Creating Uptime App in Next.js](#-4-creating-python-report-excel-generation)
5. [🛡️ 5 Implementing DevSecOps: Snyk and ZAP Scan](# 5 Implementing DevSecOps: Snyk and ZAP Scan)
6. [🌐 Setting up Google Cloud Infrastructure for Uptime App](#-5-setting-up-google-cloud-infrastructure-for-report-excel-generation)
6. [🐘 Connecting to PostgresSQL with pgAdmin](#-6-getting-a-limacharlie-organizationw)
7. [🔗 Connecting to PostgresSQL with Next](#-6-getting-a-limacharlie-organizationw)
8. [📦 Migrations](#-6-getting-a-limacharlie-organizationw)
9. [📝 Sign up](#-6-getting-a-limacharlie-organizationw)
10. [🔑 Log in](#-7-connecting-to-limacharlie-rest-api-using-postman)
11. [📊 Dashboard](#-8-authenticate)
12. [➕ Add HTTP](#-9-getting-sensors)
13. [✏️ Edit HTTP](#-9-getting-sensors)
14. [❌ Delete HTTP](#-9-getting-sensors)
15. [📡 Endpoint to receive scheduler for HTTP](#-9-getting-sensors)
16. [📈 Statistics on Dashboard](#-9-getting-sensors)
17. [👥 List Users](#-9-getting-sensors)
18. [➕ Add Users](#-9-getting-sensors)
19. [✏️ Edit Users](#-9-getting-sensors)
20. [❌ Delete Users](#-9-getting-sensors)
21. [🖥️ Running the Uptime App Locally](#%EF%B8%8F-3-running-the-finished-uptime-app-locally)
22. [☁️ Running the Uptime App on Google Cloud Run](#%EF%B8%8F-4-running-the-finished-uptime-app-on-google-cloud-run)
23. [📜 License](#-5-license)

---

## 📖 1 Learning Objectives for Uptime App

After this module you will be able to:

* Build a Full-Stack App with Next.js – Develop a complete uptime monitoring application with a responsive dashboard.

* Work with PostgreSQL & API Integration – Connect to databases, manage migrations, and integrate external APIs.

* Implement User Authentication & Role Management – Secure user access with sign-up, login, and role-based controls.

* Deploy & Scale on Google Cloud – Deploy the app using Google Cloud Run for scalability and reliability.


---

## ✨ 2 Lessons Overview for Uptime App


---


## 📸 3 Diagram and Screenshots from Uptime App

**Manage Service Diagram**
A user can add, edit and delete watchers<br>
![Uptime App - Manage Service Diagram](_docs/uptime-diagram-manage-service.drawio.png) 


**Check if services are online diagram**
A scheduler will start the application to check if services are up<br>
![Uptime App - Check if Service is Online Diagram](_docs/uptime-diagram-check-if-service-is-online.drawio.png) 

---

## ⚛️ 4 Creating Uptime App in Next.js


**1. Create new repository in Github**

* Name: **uptime-nextjs**

**2. Create new application**

Open CMD/Terminal and write:

```
mkdir next
cd next
npx create-next-app@latest
```

* What is your project name: **uptime**
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

# Build the application
ENV NODE_ENV=production

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



## 🛡️ 5 Implementing DevSecOps: Snyk and ZAP Scan

### Snyk

https://snyk.io

### ZAP Scan

.github/workflows/sec-node.yml<br>
```
name: Security for Next.js - DAST for web with OASP ZAP

on: [push]

jobs:
  dast_scan:
    runs-on: ubuntu-latest
    name: DAST (Dynamic Application Security Testing) with OASP ZAP
    steps:
      - name: ZAP Scan
        uses: zaproxy/action-full-scan@v0.10.0
        with:
          target: 'https://your-project-name-t6qfqcqcha-lz.a.run.app/'
```

---

---


## 🌐 6 Setting up Google Cloud Infrastructure for Uptime App


---

## 🐘 7 Connecting to PostgresSQL with pgAdmin

---

## 🔗 8 Connecting to PostgresSQL with Next

---

## 📦 9 Migrations

---

## 📝 10 Sign up

---


## 🔑 11 Log in


---



## 📊 12 Dashboard

---


---



## ➕ 13 Add HTTP

---



## ✏️ 14 Edit HTTP

---



## ❌ 15 Delete HTTP

---



## 📡 16 Endpoint to receive scheduler for HTTP


---



## 📈 17 Statistics on Dashboard

---



## 👥 18 List Users

---



## ➕ 19 Add Users

---



## ✏️ 20 Edit Users

---



## ❌ 21 Delete Users
---


## 🖥️ 22 Running the Uptime App Locally

---



## ☁️ 23 Running the Uptime App on Google Cloud Run



## 📜 24 License


This project is licensed under the
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**⚠️ Warning: Educational Material Only**

This repository contains projects and resources created for educational purposes as part of the Udemy course 
`Python, Next.js, PostgreSQL and DevSecOps on Google Cloud Platform with Projects from Real Industry`.

**This code is not intended for production use** and is provided **"as is"**. 
Use it at your own risk. No warranties or guarantees are provided, either express or implied. 

This material is **for students** enrolled in the course and is not meant to be used as part of any commercial product or service. 
Do not use the code as part of any production environment without thorough testing, modification, and security review.

