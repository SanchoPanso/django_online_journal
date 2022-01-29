from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.about, name='login'),
    path('anketa/', views.anketa, name='anketa'),
]