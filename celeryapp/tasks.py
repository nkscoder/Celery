from __future__ import absolute_import, unicode_literals
import time

import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')

app = Celery('celeryapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))





@app.task
def longtime_add(x, y):
    print ('long time task begins')
    # sleep 5 seconds

    time.sleep(5)
    print ('long time task finished')
    return x + y

