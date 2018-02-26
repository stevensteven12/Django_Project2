from __future__ import absolute_import, unicode_literals
from celery import task
from celery import shared_task
from django.shortcuts import render
from channels import Channel


@shared_task
def home_print(request, template="home.html"):
#    message = {}
    message = {'name': 'Print the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
    Channel('background-hello').send(message)

#    return render(request, template, dict(),)
    return render(request, template, locals(),)