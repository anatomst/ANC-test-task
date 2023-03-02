# ANC-test-task

Django project to short urls

## Deployed on pythonanywhere.com

[anatomst.pythonanywhere.com/shortner](anatomst.pythonanywhere.com/shortner)

## Admin panel

* login: admin
* password: admin

## Features

* Creating short url by API
* Creating short url in browser
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

