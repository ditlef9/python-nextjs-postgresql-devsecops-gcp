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



Table of contents:
1. [📖 Learning Objectives for News backend and Frontend](#-1-learning-objectives-for-news-backend-and-frontend)
2. [✨ Lessons Overview for News backend and Frontend](#-2-lessons-overview-for-news-backend-and-frontend)
3. [📸 Diagram and Screenshots from News backend and Frontend](#-3-diagram-and-screenshots-from-versions-tracker)
4. [🐍 Creating Python Backend](#-1-getting-started-with-news-backend-and-frontendm)
5. [⚛️ Creating Next.js Frontend](#-1-getting-started-with-news-backend-and-frontendm)
6. [🌐 Setting up Google Cloud Infrastructure for New backend and Frontend](#-1-getting-started-with-news-backend-and-frontendm)
7. [🔗 Connecting to database](#-2-registrer)
8. [🛢️ Python DBAdapter](#-2-registrer)
9. [📝 Register](#-2-registrer)
10. [🔑 Login](#-2-registrer)
11. [📰 New news](#-2-registrer))
12. [📃 List news](#-2-registrer))
13. [✏️ Edit news](#-2-registrer))
14. [🗑️ Delete news](#-2-registrer)
15. [🖥️ Running the Finished News Backend and Frontend Locally](#%EF%B8%8F-4-running-the-finished-news-backend-and-frontend-locally)
16. [☁️ Running the Finished News Backend and Frontend on Google Cloud Run](#%EF%B8%8F-5-running-the-finished-news-backend-and-frontend-on-google-cloud-run)
17. [📜 License](#-6-license)

---

## 📖 1 Learning Objectives for News backend and Frontend

* Build a **Flask-based backend**  with user authentication and a PostgreSQL database.
* Develop a **Next.js frontend** to interact with the backend API.
* Deploy the application on Google Cloud using **Cloud Run** and **PostgreSQL**.
* **Secure APIs** and authentication with best practices.


---

## ✨ 2 Lessons Overview for News backend and Frontend


1. **Introduction**

2. **Creating Python Backend**<br>
- Setting up a Flask-based backend and structuring the project.
- Activity/Reflection: What challenges did you face while setting up the backend?


3. **Creating Next.js Frontend**<br>
- Setting up a Next.js project and creating the UI components.
- Activity/Reflection: How does the frontend connect with the backend?


4. **Setting up Google Cloud Infrastructure for New backend and Frontend**<br>
- Configuring Cloud Run, PostgreSQL, and Secret Manager.
- Activity/Reflection: What are the key advantages of deploying on Google Cloud?

5. **Connecting to database**<br>
- Establishing a secure connection between your computer and and PostgreSQL.
- Activity/Reflection: Why is database security important in production?


6. **Python DBAdapter**<br>
- Establishing a secure connection between Flask and PostgreSQL.
- Activity/Reflection: How can database abstraction improve maintainability?


7. **Register**<br>
- Implementing user registration with validation and password hashing.
- Activity/Reflection: What security measures should be in place for user registration?

8. **Login**<br>
- Authenticating users and managing sessions/tokens.
- Activity/Reflection: What authentication method did you choose and why?

9. **Create news**<br>
- Creating an API to add news articles with authentication.
- Activity/Reflection: What data validation checks are necessary for posting news?

10. **List news**<br>
- Implementing an API to fetch and display news articles.
- Activity/Reflection: How does pagination improve user experience?

11. **Edit news**<br>
- Allowing authorized users to update existing news articles.
- Activity/Reflection: How do you handle permissions for editing content?

12. **Delete news**<br>
- Implementing secure deletion of news articles.
- Activity/Reflection: What precautions should be taken when deleting records?

13. **Congratulations and Learning Tip**<br>
- Learning tip: ?
- Reflection: ?

14. **Quiz**

---

## 📸 3 Diagram and Screenshots from News backend and Frontend

**News Backend and Frontend Diagram**<br>
This diagram shows the structure and flow of the Version Tracker, outlining its components and how user data is processed.<br>
![News Backend and Frontend Diagram](_docs/news-diagram.drawio.png) 


---

## 🐍 4 Creating Python Backend


**1. Create new application in Github**

* Name: news-backend-python


**2. Open application in PyCharm**

Pycharm > File > Close Project<br><br>

Pycharm > Get from VCS<br><br>


**3. Create certificates**


**4. Add requirements.txt**

```
functions-framework         # Added by YOUR_NAME. Framework for running Google Cloud Functions locally.
google-cloud-storage        # Added by YOUR_NAME. Interact with Google Cloud Storage for file operations.
```

**5. Create main.py**

```python


```

**6. Install requirements**

PyCharm > Terminal:

`pip install -r requirements.txt`



**6. Run application**<br>
In PyCharm go to main.py and click `Run`



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
* Name: **versions-tracker-bucket**
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

