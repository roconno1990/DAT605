"""teamEProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from project import views as project_views
 
urlpatterns = [
    url(r'^$', auth_views.login),
    url(r'^logout/$', project_views.logout_page),
    url(r'^accounts/login/$', auth_views.login), # If user is not login it will redirect to login page
    url(r'^register/$', project_views.register),
    url(r'^register/success/$', project_views.register_success),
    url(r'^home/$', project_views.home),
    url(r'^admin/', admin.site.urls),
]
