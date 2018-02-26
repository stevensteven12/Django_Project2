from django.shortcuts import render
from channels import Channel

"""
def home(request, template="home.html"):
#    message = {}
    message = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
    Channel('background-hello').send(message)

#    return render(request, template, dict(),)
    return render(request, template, locals(),)



def home(request, template="home.html"):
    message = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
    Channel('background-hello').send(message)

#    return render(request, template, dict(),)
    return render(request, template, locals(),)
"""