from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=80)
    dyn_attr = models.JSONField(null=True, blank=True)
    percent = models.PositiveIntegerField(default=0, blank=True)
    initial_price = models.PositiveIntegerField(default=0, blank=True)
    stock = models.SmallIntegerField(default=0)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_image', null=True, blank=True)

    def __str__(self):
        return self.product_name

    @property
    def generate_final_price(self):
        """
        final_price = Result of initial price deduction from discount percent
        """
        final_price = self.initial_price - (self.initial_price * (self.percent / 100))
        return final_price
