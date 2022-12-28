from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=64, null=False)
    location_description = models.CharField(max_length=64, null=False)

class Health_description(models.Model):
    health_level = models.IntegerField(null=False)
    health_description = models.CharField(max_length=64, null=False)


class Animal(models.Model):
    animal_name = models.CharField(max_length=64, null=False)
    specie = models.CharField(max_length=32, null=False)
    age = models.SmallIntegerField(null=False)
    gender = models.CharField(max_length=32, null=False)
    health = models.IntegerField(null=False)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    appearance_date = models.DateTimeField(null=False)
    photo = models.ImageField(upload_to='product_image', null=True, blank=True)

    # def __str__(self):
    #     return self.createdAt
    def __str__(self):
        return self.animal_name

