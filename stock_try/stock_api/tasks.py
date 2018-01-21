# Python Code
# project/myapp/tasks.py

import datetime
import celery
from celery import Celery, task

#celery = Celery('stock_try', broker='amqp://guest@localhost//')

@celery.decorators.periodic_task(run_every=datetime.timedelta(seconds=5)) # here we assume we want it to be run every 5 mins
def myTask():
    # Do something here
    # like accessing remote apis,
    # calculating resource intensive computational data
    # and store in cache
    # or anything you please
    print('This wasn\'t so difficult')


@celery.task
def send_email(email, token):
    print("sending email...")
    print("you can saving a file or log a message here to verify it.")


@task()
def add(x, y):
    return x + y