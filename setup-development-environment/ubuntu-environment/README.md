# ![Ubuntu](https://raw.githubusercontent.com/ditlef9/python-nextjs-postgresql-devsecops-gcp/main/_docs/ubuntu-32x23.png)  Section 1 · Lesson 7 · Setup Development Environment - Ubuntu 

[🏠 Home](../../)
&nbsp; &nbsp;
[⬅ Setup Development Environment (Software installation guide)](../../#%EF%B8%8F-2-setup-development-environment-software-installation-guide)

This guide will show you how to download and install software needed for the course
`Python and Next.js on Google Cloud Platform with Projects from Real Industry Video`.


## 1 Git

Git is a version control system to manage your code and collaborate with others.


## 1 Git on Ubuntu:**

```bash
sudo apt update
sudo apt install git -y
git --version  # Verify installation
```

---

## 2 Python on Ubuntu

Python is a popular programming language for backend development and automation.

**Installation Steps:**

```bash
sudo apt update
sudo apt install python3 python3-pip -y
python3 --version  # Verify installation
pip3 --version  # Verify pip installation
```

---

## 3 Node.js

Node.js is a JavaScript runtime used for building server-side applications.


**Installation Steps:**

```bash
sudo apt update
sudo apt install nodejs npm -y
node -v  # Verify Node.js installation
npm -v  # Verify npm installation
```

---

## 4 VSCode

VSCode is a lightweight, powerful code editor for various programming languages. We will use it to develop Next.js applications.

**Installation Steps with Ubuntu App Center:**

App Center > Search for `code` > Install


**Installation Steps with command line:**
```bash
sudo apt update
sudo apt install wget gpg -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /usr/share/keyrings/packages.microsoft.gpg > /dev/null
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt install code -y
code --version  # Verify installation
```


---

## 5 PyCharm


PyCharm is an IDE specifically designed for Python development.

**Installation Steps with Ubuntu App Center:**

App Center > Search for `pycharm` > Install


**Installation Steps with command line:**


```bash
sudo snap install pycharm-community --classic
```

---

## 6 PostgreSQL

PostgreSQL is an open-source relational database system. The course will use the following password and port:

* Password: root
* Port: 5432


**Installation Steps with Ubuntu App Center:**

App Center > Search for `postgresql` > Install

**Installation Steps with command line:**
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
sudo -u postgres psql
ALTER USER postgres PASSWORD 'root';
\q  # Exit PostgreSQL
```

Find `local all postgres peer` and replace `peer` with `md5`. Save the file and restart PostgreSQL:
```bash
sudo systemctl restart postgresql
```

How to Install pgAdmin on Ubuntu

### After installing PostgreSQL, follow these steps to install pgAdmin:

**1. Add the pgAdmin Repository*'

Run the following commands:

```bash
sudo apt update
sudo apt install curl ca-certificates gnupg -y
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/pgadmin-keyring.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/pgadmin-keyring.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```

**2. Install pgAdmin**

For the desktop mode (GUI version), install:
```bash
sudo apt install pgadmin4 -y
```

**3. Launch pgAdmin**

Desktop Mode: Run pgAdmin from the application menu

---

## 7 Google Cloud CLI

Google Cloud CLI is a command-line tool for managing Google Cloud resources.

**Installation Steps with Ubuntu App Center:**

App Center > Search for `google-cloud-cli` > Install

**Installation Steps with command line:**

```
sudo apt update
sudo apt install curl -y
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-$(curl -s https://dl.google.com/dl/cloudsdk/channels/rapid/components-2.json | grep version | head -1 | cut -d '"' -f 4)-linux-x86_64.tar.gz
tar -xvzf google-cloud-cli-*.tar.gz
./google-cloud-sdk/install.sh
./google-cloud-sdk/bin/gcloud init  # Configure Google Cloud SDK
d```


---

## 8 Docker Desktop


Docker Desktop allows you to create and manage containers for your development environment.

Installation of Docker Desktop is optional but recommend for debugging purposes.


**Installation Steps with Ubuntu App Center:**

App Center > Search for `docker` > Install


**Installation Steps with command line:**

Run the following commands in the terminal:

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

Add your user to the Docker group to run it without sudo:

```bash
sudo usermod -aG docker $USER
newgrp docker
docker --version  # Verify installation

```