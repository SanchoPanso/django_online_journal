"""online_journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include as include_admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('contact/', include('app.urls')),
    path('about/',  include('app.urls')),
    path('blog/', include('app.urls')),
    path(r'<parameter>/', include('app.urls')),
    path('login/', include('app.urls')),
    path('anketa/', include('app.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', include('app.urls')),
]
