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

Configure Mail Auth Settings

> 8

Configure mail templates

> 9 

Create an app named `sendmail`

> 10 

Define a simple python function named send_mail() and paste the below code, replace mail with yours.

```python
from dbmail import send_db_mail
# Create your views here.


def send_mail():

	send_db_mail(
	    # slug - which defined on db template
	    'welcome-template',

	    # recipient can be list, or str separated with comma or simple string
	    # 'user1@example.com' or 'user1@example.com, user2@example.com' or
	    # ['user1@example.com', 'user2@example.com'] or string Mail group slug
	    'rishikesh@servirall.in',

	    # All *args params will be accessible on template context
	    {
	        'first_name': 'Rishikesh'
	    },

	    # You can access to all model fields. For m2m and fk fields, you should use module_name
	    # MyModel.objects.get(pk=1),

	    #######################################################################
	    ### Optional kwargs:
	    #######################################################################
	    # from_email='',
	    cc=['rishikesh@moneybloom.in'],
	    bcc=['rishikesh0011115067@gmail.com'],

	    # # For store on mail logs
	    # user=User.objects.get(pk=1),

	    # # Current language code, which selected by user
	    # language='ru',

	    # # This options is documented on the Django docs
	    # attachments=[(filename, content, mimetype)],
	    # files=['hello.jpg', 'world.png'],
	    # headers={'Custom-Header':'Some value'},

	    # # For working with different queue, you can specify queue name on the settings, or on option
	    # queue='default',

	    # # Time for retry failed send. Working with celery only
	    # retry_delay=300,

	    # # Max retries, when sending is failed
	    # max_retries=3,

	    # # You can disable retry function
	    # retry=True,

	    # # Hard limit on seconds
	    # time_limit=30,

	    # # Postpone send email for specified seconds
	    # send_after=60,

	    # # You can disable celery for debug messages, or when error is occurred,
	    # # and email can not be delivered by celery.
	    # # Or some part of your app run on instance, where celery is not used.
	    # use_celery=True,

	    # # ...
	    # # another named arguments, which supported by specified backend
	    # # ...
	)
```


> 11

Open shell using `python manage.py shell`


> 12

Finally, execute the below commands

```python
from sendmail import views as v

v.send_mail()
```

> 13

Check the status on Admin panel (Mail logs)

That is it.