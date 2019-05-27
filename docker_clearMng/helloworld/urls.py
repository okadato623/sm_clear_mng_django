from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.send_words, name='hello world'),
    path('admin/', admin.site.urls),
]