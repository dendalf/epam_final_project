# Library site

[![Build Status](https://app.travis-ci.com/dendalf/epam_final_project.svg?branch=main)

This is Library site where you can store and read books. It provides a platform for library workers to create and manage their books and authors. It uses RESTful web service to perform CRUD operations.

## With this app you can:

- Display a list of books with title, author, published date, price, also you can search books by its published date.
- Display the list of authors with first name, last name, birthdate, average book price, calculated automatically.
- Change (add / edit / delete / get detail of) the above data.

## Getting started

Before you start using the application, please ensure that you have Python 3.9 installed on your system.

## How to build this project:

### Clone the repo:

```
git clone https://github.com/dendalf/epam_final_project.git
```

### Navigate to the epam_final_project directory using the following command:

```
cd epam_final_project
```

### Create the virtual environment in project:

```
python3 -m virtualenv venv
source env/bin/activate
```

### Install project requirements:

```
pip install -r requirements.txt
```

### Configure MySQL database

#### Create .env file and set the following environment variables:

```
FLASK_APP=runner.py
SECRET_KEY=wfsmlksfscdlce
DATABASE_URI=mysql+pymysql://<your_mysql_user>:<your_mysql_user_password>@localhost:3306/<your_mysql_database_name>

MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_user_password>
MYSQL_SERVER=<your_mysql_server>
MYSQL_DATABASE=<your_mysql_database_name>
```

#### Log in to MySQL using the following command:

```
sudo mysql -u root -p
```

#### Create new database named book

```
CREATE DATABASE book;
```

#### If necessary, initialize and create migrations using the following commands:

```
flask db init
flask db migrate
flask db upgrade
```

#### Run the application using:

```
flask run
```

## Now you should be able to access the web application on the following addresses:

### Web Application:

```
localhost:5000/
localhost:5000/book/list
localhost:5000/book/list?date_published_start=2023-03-14&date_published_end=2023-03-16
localhost:5000/book/create
localhost:5000/book/update/<id>
localhost:5000/book/delete/<id>
localhost:5000/book/detail/<id>
localhost:5000/author/list
localhost:5000/author/create
localhost:5000/author/update/<id>
localhost:5000/author/delete/<id>
localhost:5000/author/detail/<id>
```
