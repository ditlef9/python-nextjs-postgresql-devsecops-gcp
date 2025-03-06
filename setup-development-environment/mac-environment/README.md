# ![Mac](https://raw.githubusercontent.com/ditlef9/python-nextjs-postgresql-devsecops-gcp/main/_docs/mac-32x23.png)  Section 1 · Lesson 8 · Setup Development Environment - Mac 

![🏠 Home](../../)
&nbsp; &nbsp;
![⬅ Setup Development Environment (Software installation guide)](../../#%EF%B8%8F-2-setup-development-environment-software-installation-guide)

This guide will show you how to download and install software needed for the course
`Python and Next.js on Google Cloud Platform with Projects from Real Industry Video`.


## 1 Git

Git is a version control system to manage your code and collaborate with others.


## 1 Git on Ubuntu:**

```bash
brew install git
git --version  # Verify installation
```

---

## 2 Python on Ubuntu

Python is a popular programming language for backend development and automation.

**Installation Steps:**

```bash
brew install python3
python3 --version  # Verify installation
pip3 --version  # Verify pip installation
```

---

## 3 Node.js

Node.js is a JavaScript runtime used for building server-side applications.


**Installation Steps:**

```bash
brew install node
node -v  # Verify Node.js installation
npm -v  # Verify npm installation
```

---

## 4 VSCode

VSCode is a lightweight, powerful code editor for various programming languages. We will use it to develop Next.js applications.


**Installation Steps:**
```bash
brew install --cask visual-studio-code
code --version  # Verify installation
```


---

## 5 PyCharm


PyCharm is an IDE specifically designed for Python development.


**Installation Steps:**

```bash
brew install --cask pycharm
```

---

## 6 PostgreSQL

PostgreSQL is an open-source relational database system. The course will use the following password and port:

* Password: root
* Port: 5432


**Installation Steps:**
```bash
brew install postgresql
brew services start postgresql
```


Set password for **Postgres** user:
```bash
psql postgres
ALTER USER postgres PASSWORD 'root';
\q  # Exit PostgreSQL
```

### After installing PostgreSQL, follow these steps to install pgAdmin:


```bash
brew install --cask pgadmin4
```


---

## 7 Google Cloud CLI

Google Cloud CLI is a command-line tool for managing Google Cloud resources.


**Installation Steps:**


```
brew install --cask google-cloud-sdk
gcloud init  # Configure Google Cloud SDK
```


---

## 8 Docker Desktop


Docker Desktop allows you to create and manage containers for your development environment.

Installation of Docker Desktop is optional but recommend for debugging purposes.



**Installation Steps:**

Run the following commands in the terminal:

```bash
brew install --cask docker
open /Applications/Docker.app  # Start Docker
```

Verify installation:

```bash
docker --version

```