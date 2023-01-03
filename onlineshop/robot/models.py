from django.db import models
from django.contrib.auth.models import User
from product.models import Animal



class Robot_description(models.Model):
    # robot_id = models.ForeignKey(Robot, on_delete=models.CASCADE, primary_key=True)
    size = models.CharField(max_length=32, null=True, blank=True)
    color = models.CharField(max_length=32, null=True, blank=True)

class Robot(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    # status = models.BooleanField(null=True, blank=True)
    damage_level = models.IntegerField(null=True, blank=True)
    animal = models.ManyToManyField(Animal, null=True, blank=True)
    robot_descr = models.ForeignKey(Robot_description, on_delete=models.CASCADE)