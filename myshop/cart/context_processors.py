# -*- coding:utf-8 -*-
# @Time: 2020/8/31 9:51
# @Author: Lj
# @File: context_processors.py

from .cart import Cart

def cart(request):
    return {'cart':Cart(request)}