from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hi', views.test, name='test'),
    path('hello', views.test2, name='test2'),
    path('many/', views.many, name='many'),
    path('mylocate/', views.mylocate, name='mylocate'),
     path('search', views.search, name='search'),
]
