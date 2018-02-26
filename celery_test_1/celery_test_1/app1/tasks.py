from __future__ import absolute_import, unicode_literals
from celery import task
from celery import shared_task
from django.core.mail import send_mail
from celery import task
from .models import LogEntry


@task
def hello_world():
    with open("output.txt", "a") as f:
        f.write("hello world")
        f.write("\n")
    print("hello world")


@shared_task
def task_mail():
    subject = 'subject test'
    message = 'message test'
    mail_sent = send_mail(subject,
                          message,
                          'admin@celery_test.com',
                          ['steven@pkinno.com',])
    return mail_sent


@task()
def write_log_entry(severity, message):
    """
    Write a log entry to the database
    """
    log = LogEntry(severity=severity, message=message)
    log.save()