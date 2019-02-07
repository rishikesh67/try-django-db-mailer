from django.shortcuts import render
from dbmail import send_db_mail
# Create your views here.


def send_mail():

	send_db_mail(
	    # slug - which defined on db template
	    'welcome-template',

	    # recipient can be list, or str separated with comma or simple string
	    # 'user1@example.com' or 'user1@example.com, user2@example.com' or
	    # ['user1@example.com', 'user2@example.com'] or string Mail group slug
	    'rishikesh@moneybloom.in',

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