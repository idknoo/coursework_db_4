from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from account.models import Account

class Passport(models.Model):
    series_passport = models.IntegerField(blank=True,null=True)
    number_passport = models.IntegerField(blank=True,null=True)
    passport_issue = models.CharField(max_length=200,blank=True,null=True)
    date_issue = models.DateTimeField(blank=True,null=True)

class Customer(User):
    phone = PhoneNumberField(null=True, blank=True)
    address = models.TextField(max_length=400, null=True, blank=True)
    name = models.CharField(max_length=45,blank=True,null=True)
    surname = models.CharField(max_length=45,blank=True,null=True)
    patronymic = models.CharField(max_length=45, blank=True,null=True)
    date_birthday = models.DateTimeField(blank=True, null=True)
    gender = models.BooleanField(blank=True,null=True)
    passport_id = models.ForeignKey(Passport, blank=True, null=True, on_delete=models.CASCADE)


    def full_name(self):
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.username}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')

