import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chattapp.settings')
celery = Celery('chattapp')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()