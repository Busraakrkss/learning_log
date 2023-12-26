from django.shortcuts import render

from .models import Topik


# Create your views here.
def index(request):
    """The home page for learning log."""
    return render(request, 'learning_logs/index.html')


def topiks(request):
    topiks = Topik.objects.order_by('date_added')
    context = {'topiks': topiks}
    return render(request, 'learning_logs/topiks.html', context)

