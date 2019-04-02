from celery import Celery
celery = Celery('swagger_server', broker='redis://127.0.0.1:6379/0')
