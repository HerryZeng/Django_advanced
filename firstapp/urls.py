#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path,include
from firstapp import views
urlpatterns = [
    path('',views.home,name='home'),
]