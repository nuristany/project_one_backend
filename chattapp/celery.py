import os
from celery import Celery

os.environ.setdefault('DJANGO.SETTINGS.MODULE', 'chattapp.settings')
celery = Celery('chattaapp')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()