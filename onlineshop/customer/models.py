from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from account.models import Account


class Customer(User):
    phone = PhoneNumberField(null=True, blank=True)
    address = models.TextField(max_length=400, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.username}"


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='coupon')
    expire_date = models.DateTimeField()

    def __str__(self):
        return f"{self.customer}'s coupon"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
