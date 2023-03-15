from django.shortcuts import render

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
