from __future__ import absolute_import, unicode_literals
from celery import task
from django.shortcuts import render_to_response, HttpResponse

@task
def hello_world():
    with open("output.txt", "a") as f:
        f.write("hello world")
        f.write("\n")
    print("hello world")


@task
def meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單

    sorted(values)

    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))