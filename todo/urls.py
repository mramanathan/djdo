"""djdo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'index/$', views.index, name='index'),
    url(r'todo/$', views.todo_list, name='todo_list'),
    url(r'todo/(?P<pk>[0-9]+)/$', views.todo_detail, name='todo_detail'),
    url(r'todo/new/$', views.todo_new, name='todo_new'),
    url(r'todo/(?P<pk>[0-9]+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'todo/(?P<pk>[0-9]+)/delete/$', views.todo_delete, name='todo_delete'),
]
