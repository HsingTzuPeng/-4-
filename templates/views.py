from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Product, Order, OrderItem

from django.http import JsonResponse
from django.views import View
from django.core import serializers
from .models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class OrderFormView(FormView):
    template_name = 'order_form.html'
    form_class = OrderForm
    success_url = '/thankyou/'

    def form_valid(self, form):
        order = Order.objects.create(
            customer_name=form.cleaned_data['name'],
            customer_email=form.cleaned_data['email']
        )
        for product_id, quantity in form.cleaned_data['products'].items():
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )
        return super().form_valid(form)


class ProductJsonView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = serializers.serialize('json', products)
        return JsonResponse(data, safe=False)
