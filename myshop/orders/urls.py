# -*- coding:utf-8 -*-
# @Time: 2020/8/31 11:22
# @Author: Lj
# @File: urls.py
from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.oder_create, name='order_create'),
    path('admin/order/<int:order_id>', views.admin_order_detail,
         name='admin_order_detail'),
]