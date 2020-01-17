from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, 'new.html')
def map(request):
    return render(request, 'map.html')
def mapmap(request):
    return render(request, 'mapmap.html')

