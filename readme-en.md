# Default README for my projects

[Português](https://github.com/Tche-Marco/opencv/blob/master/README.md)

<h1>Project Name</h1>

> Status: Developing

### This project is a WEB application created with the intention of...

## Project's class models:

- User (a class to represent a user)
- Class name (a class to represent a object)

### Main attributes:

- User: name (first name of the user)
- User: mail (mail of the user)
- User: birth (birth date of the user)
- User: active (user is active?)
- Class name: field (field description)

### Methods for implementing some features, such as:

- Message of success when create a User.
- Functions to manage user profile.
- Function to get age from birthday.

## This features are in developing:

- Account verification and password change via email.

## Technologies Used:

<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>PostgreSQL</td>
  </tr>
  <tr>
    <td>3.10</td>
    <td>3.2</td>
    <td>12</td>
  </tr>
</table>

## How to run the application:

create and activate a python virtual environment

```console
  python -m venv venv
```

```console
  venv\Scripts\activate | windows
  .venv/bin/activate | linux e macOs
```

Install all project dependencies

```console
  pip install -r requirements.txt
```

Set default values for environment variables (.env)

```
  Copy the file .env.example and rename it to .env
```

Configuring the local database

```
  Database is being hosted locally, to configure the accesses, use the .env file and enter your local bank login information.
```

Config example

```
  SECRET_KEY=Your Django key
  DEBUG=True
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME=database name
  DB_USER=database user
  DB_PASSWORD=database password
  DB_HOST=database host (default='localhost')
  DB_PORT=database port (default=5432)
```

## Use

Pass the models to the database:

```console
python manage.py makemigrations
```

```console
python manage.py migrate
```

Run the server:

```console
python manage.py runserver 8000
```

The server will be available at:

```console
http://127.0.0.1:8000/
```
