from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    products = models.ManyToManyField(Product, through='OrderItem')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
