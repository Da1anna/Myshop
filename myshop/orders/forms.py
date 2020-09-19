# -*- coding:utf-8 -*-
# @Time: 2020/8/31 10:16
# @Author: Lj
# @File: forms.py
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
