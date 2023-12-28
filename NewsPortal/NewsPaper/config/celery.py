import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'every_monday_task': {
        'task': 'news.tasks.weekly_mailing',
        'schedule': crontab(hour=8, minute=00, day_of_week='monday'),
#        'schedule': crontab(),
    }
}

app.autodiscover_tasks()
