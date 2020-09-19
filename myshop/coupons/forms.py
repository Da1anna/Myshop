# -*- coding:utf-8 -*-
# @Time: 2020/9/3 10:07
# @Author: Lj
# @File: forms.py

from django import forms

class CouponApplyForm(forms.Form):
    code = forms.CharField()
