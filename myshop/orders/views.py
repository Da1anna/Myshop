from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def oder_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            #清空购物车
            cart.clear()
            context = {'order': order}
            #set the order in the session
            request.session['order_id'] = order.id
            #重定向到支付界面
            return redirect(reverse('payment:process'))
            # return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreateForm()
        context = {'cart': cart, 'form': form}
        return render(request, 'orders/order/create.html', context)

@staff_member_required
def admin_order_detail(request, order_id):
    '''在管理界面显示订单详情的视图'''
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html',
                  {'order': order})