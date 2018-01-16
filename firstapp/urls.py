#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path, re_path
from django.views.generic import RedirectView

from firstapp import views
from .forms import AddTaskForm, AddPoemForm
from .views import IndexView, ShowTasksView, DisplaySingleView, AddModelView, ShowPoemView

urlpatterns = [
    path('', views.home, name='home'),
    # path('index/',views.index,name='index'),
    # path('index/', TemplateView.as_view(template_name='firstapp/index.html'), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('redirect/', RedirectView.as_view(url='http://www.baidu.com')),
    path('tasklist/', ShowTasksView.as_view(),name='tasklist'),
    path('poemlist/', ShowPoemView.as_view(),name='poemlist'),
    re_path("task/(?P<task_id>\d+)/?$", DisplaySingleView.as_view(),name = 'task'),
    path('add_poem/', AddModelView.as_view(form_class=AddPoemForm, template_name='firstapp/add_poem.html',
                                           return_url='/poemlist/'),name='add_poem'),
    path('add_task/', AddModelView.as_view(form_class=AddTaskForm, template_name='firstapp/add_task.html',
                                           return_url='/tasklist/'),name='add_task'),
]
