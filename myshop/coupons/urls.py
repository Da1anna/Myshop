# -*- coding:utf-8 -*-
# @Time: 2020/9/3 10:20
# @Author: Lj
# @File: urls.py

from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),
]