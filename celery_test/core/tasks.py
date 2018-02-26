import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import task
from celery import shared_task
from django.core.mail import send_mail


@task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task
def task_mail():
    subject = 'subject test'
    message = 'message test'
    mail_sent = send_mail(subject,
                          message,
                          'admin@celery_test.com',
                          ['steven@pkinno.com'])
    return mail_sent