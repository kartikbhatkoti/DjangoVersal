#First step create urls.py under home app
#copied from 
from django.contrib import admin
from django.urls import path
#imported seperately

from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.about, name='contact'),
    path('services', views.about, name='services')
]
