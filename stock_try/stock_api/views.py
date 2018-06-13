from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render, render_to_response, HttpResponseRedirect

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.embed import file_html
import time
import threading


from .models import Question


def index(request):
    # prepare some data
    x = [0.2, 0.4, 0.6, 0.8, 2.0, 2.5, 3.0]
    y0 = [i ** 2 for i in x]
    y1 = [10 ** i for i in x]
    y2 = [10 ** (i ** 2) for i in x]

    # output to static HTML file
    output_file("stock_api/index.html")

    # create a new plot
    p = figure(
        tools="pan,box_zoom,reset,save",
        y_axis_type="log", y_range=[0.001, 10 ** 11], title="log axis example",
        x_axis_label='sections', y_axis_label='particles'
    )

    # add some renderers
    p.line(x, x, legend="y=x")
    p.circle(x, x, legend="y=x", fill_color="white", size=8)
    p.line(x, y0, legend="y=x^2", line_width=3)
    p.line(x, y1, legend="y=10^x", line_color="red")
    p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

    # show the results
    # show(p)  # this will create another html file to show

    #Feed them to the Django template.
    return render_to_response('stock_api/index.html')

def index_1(request):
    x = [1, 3, 5, 7, 9, 11, 13]
    y = [1, 2, 3, 4, 5, 6, 7]
    title = 'y = f(x)'

    plot = figure(title=title,
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=400,
                  plot_height=400)

    plot.line(x, y, legend='f(x)', line_width=2)
    # Store components
    script, div = components(plot)

    # Feed them to the Django template.
    return render_to_response('stock_api/index_1.html',
                              {'script': script, 'div': div})

def index_2(request):
    x = [1, 3, 5, 7, 9, 11, 13]
    y = [1, 2, 3, 4, 5, 6, 7]
    title = 'y = f(x)'

    plot = figure(title=title,
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=400,
                  plot_height=400)

    plot.line(x, y, legend='f(x)', line_width=2)
    # Store components
    script, div = components(plot)

    # Feed them to the Django template.
    return render_to_response('stock_api/index_1.html',
                              {'script': script, 'div': div})

def menu(request):
#    food = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
#    return render_to_response('stock_api/menu.html', locals())

    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False, 'Papular': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True, 'Papular': True}
    foods = [food1, food2]
#    foods = []
    return render_to_response('stock_api/menu.html', locals())

def draw_line(request):
    """"
    with open('stock_api/IndexTable_TX00.Txt') as f:
        lines = f.readlines()
    f.close()
"""
    words= []
    wholeline= []
    x= []
    y = []
    with open('stock_api/IndexTable_TX00.Txt') as f:
        for line in f:
            word = line.split(",")
            wholeline.append(line)
            words.append(word[0])
            x.append(word[0])
            y.append(word[4])

    return render_to_response('stock_api\draw_line.html', {'mylist': words, 'line_list': wholeline, 'x': x, 'y': y})


def draw_line_2(request):
    words = []
    x = []
    y = []
    with open('stock_api/IndexTable_TX00.Txt') as f:
        for line in f:
            word = line.split(",")
            words.append(word[0])
            x.append(word[0])
            y.append(word[4])

    title = 'y = f(x)'
    plot = figure(title=title,
                  x_axis_label='X-Axis',
                  y_axis_label='Y-Axis',
                  plot_width=400,
                  plot_height=400)

    plot.line(x, y, legend='f(x)', line_width=2)
    # Store components
    script, div = components(plot)

#    html = file_html(plot, CDN, "stock_api/line_2.html")
#    new_path = 'stock_api/templates/stock_api/line_2.html'
#    new_file = open(new_path, 'w')
#    new_file.write(html)

#    myTask()
    # Feed them to the Django template.
    return render_to_response('stock_api/line_2.html',
                              {'script': script, 'div': div})


def draw_line_3(request):
    threading.Timer(5.0, draw_line_2).start()
    print
    "Hello, World!"



#    return HttpResponseRedirect("draw_line_2")

""""
for i in range(10):
    index_2()
    time.sleep(1)
"""

"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)