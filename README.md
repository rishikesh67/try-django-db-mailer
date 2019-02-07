# try-django-db-mailer

> 1

```bash
pip install django-db-mailer
```

> 2 - Adding 2 more entries and setting SITE_ID

```python
INSTALLED_APPS = [
	# Old
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Newly added
    'django.contrib.sites',
    'dbmail'
]

SITE_ID = 1
```

> 3

```bash
python manage.py migrate
```

> 4

```bash
pip install redis django-pylibmc
```

> 5

```python
# settings.py
CACHES = {
    # Memcached
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
    }
    # ,
    # # or Redis
    # "default": {
    #     'BACKEND': 'redis_cache.cache.RedisCache',
    #     'LOCATION': '127.0.0.1:6379:2',
    # },
    # # or Memory
    # "default": {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'unique-snowflake'
    # },
}
```

**Note:** App do not work without caches

> 6

**Note:** If `pytz` is not installed and if you will try to access `Email Templates` app on Admin interface, it will raise exception like below.

```bash
...
    raise ImproperlyConfigured("This query requires pytz, but it isn't installed.")
ImproperlyConfigured: This query requires pytz, but it isn't installed.
```

So

```bash
pip install pytz
```

> 7

