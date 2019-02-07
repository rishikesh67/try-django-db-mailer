# try-django-db-mailer

> 1

`pip install django-db-mailer`

> 2

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Added
    'django.contrib.sites',
    'dbmail'
]

SITE_ID = 1
```

> 3

`python manage.py migrate`

> 4

``