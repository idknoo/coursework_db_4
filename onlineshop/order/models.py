from django.db import models
from customer.models import Customer
from product.models import Animal


class OrderItem(models.Model):
    product = models.ForeignKey(Animal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_item = models.ManyToManyField(OrderItem)

    ACCEPTED = 'ACCEPTED'
    DENIED = 'DENIED'
    IN_WORK = 'IN WORK'
    status_choices = (
        (ACCEPTED, 'ACCEPTED'),
        (DENIED, 'DENIED'),
        (IN_WORK, 'IN WORK')
    )
    status = models.CharField(choices=status_choices, max_length=100, default=IN_WORK)

    def __str__(self):
        return str(self.id)


class Work_shedule(models.Model):
    order_id = models.ForeignKey(Order, null=False, on_delete=models.CASCADE, primary_key=True)
    TIME = models.DateTimeField(blank=True,null=True)