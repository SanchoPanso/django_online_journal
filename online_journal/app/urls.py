from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

from . import views, forms

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('anketa/', views.anketa, name='anketa'),
    path('blog/', views.blog, name='blog'),
    path(r'<parameter>/', views.blogpost, name='blogpost'),
    path(r'registration/', views.registration, name='registration'),
    path('login/',
             LoginView.as_view
             (
                 template_name='app/login.html',
                 authentication_form=forms.BootstrapAuthenticationForm,
                 extra_context=
                 {
                     'title': 'Log in',
                     'year': datetime.now().year,
                 }
             ),
             name='login'),
]