from django.core.mail import send_mail
from django.shortcuts import render

from .tasks import task_mail
from .models import LogEntry

from .tasks import write_log_entry
from django.http import HttpResponse

"""
def index(request):  
    log = LogEntry(severity='INFO', message='Rendering the index page')
    log.save()
    return HttpResponse('Hello!')
"""

def index(request):

    write_log_entry.delay(severity='INFO', message='Rendering the index page')
    return HttpResponse('Hello!')


def dashboard(request):
    return render(request,
                  'app1/dashboard.html')


def task_use_celery(request):
    task_mail.delay()
    return render(request,
                  'app1/process_done.html')


def task_not_use_celery(request):
    subject = 'subject test'
    message = 'message test'
    recipient = ['steven@pkinno.com']
    send_mail(subject,
              message,
              'steven@pkinno.com',
              recipient)
    return render(request, 'app1/dashboard.html')