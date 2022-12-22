from django.db import models
from customer.models import Customer
from product.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_item = models.ManyToManyField(OrderItem)
    total_price = models.PositiveIntegerField(default=0)

    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    availability_choices = (
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    )
    availability = models.CharField(choices=availability_choices, max_length=100, default=AVAILABLE)

    def __str__(self):
        return str(self.id)
