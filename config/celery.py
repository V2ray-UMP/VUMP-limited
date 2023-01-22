from __future__ import absolute_import

import os

from django.conf import settings
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    # Execute the Speed Test every 15 minutes
    'check_all_users_traffic_every_15min': {
        'task': 'check_all_users_traffic',
        'schedule': crontab(minute='*/15'),
    },
}
