from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path('map/',views.map),
    path('mapmap/',views.mapmap),
]