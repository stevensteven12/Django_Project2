from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from restaurants.models import Restaurant, Food


def menu(request):
    food1 = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
    food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
    foods = [food1,food2]
    return render_to_response('menu.html',locals())


"""
def menu(request):
    if 'id' in request.GET:
        print(type(request.GET['id']))
        r = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")
"""

def meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單

    sorted(values)

    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))


def welcome(request):
    if 'user_name' in request.GET:
        return render_to_response('welcome.html', locals())
#        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())


def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())