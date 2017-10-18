from django.shortcuts import render

from .models import Marker

# Create your views here.
def home_page(request):
    return render(request, 'mapapp/home_page.html', {})


def show_markers(request):
    ctx ={
        'markers': Marker.objects.all()
    }
    return render(request, 'test.html', ctx)
