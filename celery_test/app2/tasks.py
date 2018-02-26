from __future__ import absolute_import
from celery import task
from django.shortcuts import render


@task
def add(x, y):
    return x + y


@task
def mul(x, y):
    return x * y


@task
def xsum(numbers):
    return sum(numbers)

""""
def home(request):
    context = {
        'add': tasks.add.delay(5,2).get()

    }

    return render(request, "home.html", context)
"""