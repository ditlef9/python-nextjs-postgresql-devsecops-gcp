# ![Ubuntu](https://raw.githubusercontent.com/ditlef9/python-nextjs-postgresql-devsecops-gcp/main/_docs/ubuntu-32x23.png)  Section 1 · Lesson 7 · Setup Development Environment - Ubuntu 

[🏠 Home](../../)
&nbsp; &nbsp;
[⬅ Setup Development Environment (Software installation guide)](../../#%EF%B8%8F-2-setup-development-environment-software-installation-guide)

This guide will show you how to download and install software needed for the course
`Python and Next.js on Google Cloud Platform with Projects from Real Industry Video`.


## 1 Git on Ubuntu

```bash
sudo apt update
sudo apt install git -y
git --version  # Verify installation
```

---

## 2 Python on Ubuntu

Python is a popular programming language for backend development and automation.

**1 Installation Steps for Python:**

```bash
sudo apt update
python3 --version  # Check if Python is already installed (if it is then you do not need to install it)
sudo apt install python3 -y
```

**2 Installation Steps for pip (package installer for Python):**

```bash
sudo apt install python3-pip -y
pip3 --version  # Verify pip installation
```

---

## 3 Node.js on Ubuntu

Node.js is a JavaScript runtime used for building server-side applications.


**Installation Steps:**

```bash
sudo apt update
sudo apt install nodejs npm -y
node -v  # Verify Node.js installation
npm -v  # Verify npm installation
```

---

## 4 VSCode on Ubuntu

VSCode is a lightweight, powerful code editor for various programming languages. We will use it to develop Next.js applications.

**Installation Steps with Ubuntu App Center:**

App Center > Search for `code` > Install


---

## 5 PyCharm on Ubuntu


PyCharm is an IDE specifically designed for Python development.

**Installation Steps with Ubuntu App Center:**

App Center > Search for `pycharm` > Install



---

## 6 PostgreSQL on Ubuntu

PostgreSQL is an open-source relational database system. The course will use the following password and port:

* Password: root
* Port: 5432


**Installation Steps with command line (recommended):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

Start and enable PostgreSQL service:
```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

Set password for **Postgres** user:
```bash
sudo -u postgres psql template1
ALTER USER postgres with encrypted password 'root';
\q
```


### After installing PostgreSQL, follow these steps to install pgAdmin:


**1 Install pgAdmin from App Center**

Open App Center and serach for `pgAdmin`. Install it.

**2 Connect to Database from pgAdmin**

pgAdmin > [Right click on Servers] > Register: Server..

General:
    * Name: `localhost`

Connection:
    * Host name/address: `127.0.0.1`
    * Port: `5432`
    * Username: `postgres`
    * Password: `root`
    * Save password: `[v]`

Click [Save]


---

## 7 Google Cloud CLI on Ubuntu

Google Cloud CLI is a command-line tool for managing Google Cloud resources.

**Installation Steps with Ubuntu App Center:**

App Center > Search for `google-cloud-cli` > Install

After installing you need to Initialize it:

```bash
gcloud -v # Check installation
gcloud init # Initialize (login to Google Cloud)
```


---

## 8 Docker on Ubuntu


Docker Desktop allows you to create and manage containers for your development environment.

Installation of Docker Desktop is optional but recommend for debugging purposes.


**Installation Steps with Ubuntu App Center:**

App Center > Search for `docker` > Install

Check installation:

```bash
docker --version  # Verify installation
```