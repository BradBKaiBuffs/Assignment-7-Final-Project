# view.py for graph
from django.contrib.auth.decorators import login_required
from checksheet.models import Course
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
import numpy as np

@login_required
# def course_count(request):
#     courses = Course.objects.count()
#     numbers = [x for x in range(100)]
#
#     graph_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
#     return render(request, 'graph.html')
    # Data for plotting
def course_count(request):
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)


    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time', ylabel='voltage',
           title='time vs voltage')
    ax.grid()

    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response