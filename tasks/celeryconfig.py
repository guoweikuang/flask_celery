from __future__ import absolute_import
from kombu import Queue, Exchange


# CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
BROKER_URL = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_QUEUES = (
    Queue('default', Exchange("default"), routing_key='default'),
    Queue('crawl', Exchange('crawl'), routing_key='task_a'),
    Queue('send', Exchange('send'), routing_key='task_b')
)


CELERY_ROUTES = {
    'tasks.taskA': {
        'queue': 'crawl',
        'routing_key': 'task_a'
    },
    'tasks.taskB': {
        'queue': 'send',
        'routing_key': 'task_b'
    }
}
