# ANC-test-task

Django project to short urls

## Deployed on pythonanywhere.com

[Project on pythonanywhere ](https://anatomst.pythonanywhere.com/shortner/)

## Admin panel

* login: admin
* password: admin

## Features

* Sending POST requests to create short url by API "api/shortner/"
* Creating short url using API (input in browser) [https://anatomst.pythonanywhere.com/create-link/](https://anatomst.pythonanywhere.com/create-link/)
* Creating short url in browser (Django views)
* Get statistics of clicks

## Installation with GitHub

```shell
git clone https://github.com/anatomst/ANC-test-task.git
python3 -m venv venv
source venv/bin/activate (on Linux and macOS) or venv\Scripts\activate (on Windows)
pip install -r requirements.txt

"To run server"
"Create .env file with"

SECRET_KEY=<Django_secret_key>
DEBUG=False

python manage.py runserver
```

