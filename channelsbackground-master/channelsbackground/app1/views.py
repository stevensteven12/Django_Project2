from django.shortcuts import render
from channels import Channel
from .tasks import home_print
import requests

"""
def home(request, template="home.html"):
#    message = {}
    message = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
    Channel('background-hello').send(message)

#    return render(request, template, dict(),)
    return render(request, template, locals(),)
"""


def home(request, template="home.html"):
#    home_print.delay(request= request, template= template)

    message = {'name': 'Pusheen the Cat_3', 'country': 'USA', 'favorite_numbers': [42, 105]}
    Channel('background-hello').send(message)
    return render(request, template, locals(),)


def livelog(request):
    return render(request, 'blog.html')