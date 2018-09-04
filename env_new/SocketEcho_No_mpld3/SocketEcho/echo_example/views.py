from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse



def livelog(request):
    """""    
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1

    fig, ax = plt.subplots()
    ax.plot(x, y1)
#    plt.show()
    mpld3.fig_to_html(fig)
    mpld3.save_html(fig, 'echo_example/templates/interactive_fig.js')

    f= open('echo_example/templates/interactive_fig.js', 'r')
    content = f.read()
    f.close();
    the_file= open('test.js', 'w')
    the_file.write(content)
    the_file.close()
    """""
    return render(request, 'index.html')


def upload_data(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'echo_example/templates/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'echo_example/templates/simple_upload.html')


def download_data(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/html")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
    return render(request, 'index.html')


def file_download(request):
    # do something...
    with open('echo_example/static/IndexTable_TX00.Txt') as f:
        c = f.read()
    return HttpResponse(c)