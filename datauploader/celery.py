from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nokia.settings')

app = Celery('datauploader')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.conf.broker_url = os.getenv('REDIS_URL', 'redis://')
app.conf.result_backend = os.getenv('REDIS_URL', 'redis://')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# set the default Django settings module for the 'celery' program.
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))