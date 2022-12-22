from django.db import models


#
# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=80)
#     dyn_attr = models.JSONField(null=True, blank=True)
#     percent = models.PositiveIntegerField(default=0, blank=True)
#     initial_price = models.PositiveIntegerField(default=0, blank=True)
#     stock = models.SmallIntegerField(default=0)
#     description = models.TextField()
#     photo = models.ImageField(upload_to='product_image', null=True, blank=True)
#
#     def __str__(self):
#         return self.product_name
#
#     @property
#     def generate_final_price(self):
#         """
#         final_price = Result of initial price deduction from discount percent
#         """
#         final_price = self.initial_price - (self.initial_price * (self.percent / 100))
#         return final_price


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

