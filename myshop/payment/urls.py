# -*- coding:utf-8 -*-
# @Time: 2020/9/1 12:12
# @Author: Lj
# @File: urls.py

from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]