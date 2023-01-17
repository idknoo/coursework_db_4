from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from django.urls import reverse


class Location(models.Model):
    location_name = models.CharField(max_length=64, null=False)
    location_description = models.CharField(max_length=64, null=False)

class Health_description(models.Model):
    health_level = models.IntegerField(null=False)
    health_description = models.CharField(max_length=64, null=False)


class Animal(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()

    animal_name = models.CharField(max_length=64, null=False)
    specie = models.CharField(max_length=32, null=False)
    age = models.SmallIntegerField(null=False)
    gender = models.CharField(max_length=32, null=False)
    health = models.IntegerField(null=False)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    appearance_date = models.DateTimeField(null=False)
    photo = models.ImageField(upload_to='product_image', null=True, blank=True)
    is_given = models.BooleanField(blank=True, null=True, default=None)
    booked_by_who = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    # def __str__(self):
    #     return self.createdAt
    def __str__(self):
        return self.animal_name

