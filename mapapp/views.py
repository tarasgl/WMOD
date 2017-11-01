from django.shortcuts import render

from .models import Marker

# Create your views here.
def home_page(request):
    ctx ={
        'markers': Marker.objects.all()
    }
    return render(request, 'mapapp/home_page.html', ctx)


def show_markers(request):
    ctx ={
        'markers': Marker.objects.all()
    }
    return render(request, 'test.html', ctx)

def show_full_info(request,el_id):
    ctx={
        'marker': Marker.objects.get(id=el_id)
    }
    return render(request,'mapapp/full_info.html',ctx);
