from django.shortcuts import render



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
