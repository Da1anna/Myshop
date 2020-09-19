# -*- coding:utf-8 -*-
# @Time: 2020/8/29 16:21
# @Author: Lj
# @File: urls.py

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]