from __future__ import absolute_import, unicode_literals

# import os
#
# from celery import Celery
#
from .settings import CELERY_BROKER_URL
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')

app = Celery('celeryapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Asia/Kolkata'

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')
# app = Celery('celeryapp')
# app.config_from_object('django.conf:settings', namespace='CELERY')

app = Celery('celeryapp',
             broker=CELERY_BROKER_URL,
             backend='rpc://',
             include=['celeryapp.tasks'])
app.conf.beat_schedule = {
'testing-add': {
       'task': 'celeryapp.tasks.longtime_add',
       'schedule': crontab(hour=9, minute=10),
       'args': (16, 16),
   }
}