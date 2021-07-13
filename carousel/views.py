from django.shortcuts import render
from .models import Slider, Another , Feature



def index(request):
    feature = Feature.objects.all()
    another = Another.objects.all()
    slider = Slider.objects.all()
    context = {
        "slider": slider,
        "feature": feature,
        "another":another,
    }
    return render(request, 'index.html', context)