from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('add/', views.add, name='add'),
    path('upload/', views.upload, name='upload'),
    path('deleteAll/', views.deleteAll, name='deleteAll'),
    path('misc', views.misc, name='misc'),
    path(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]