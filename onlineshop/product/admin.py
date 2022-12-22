from django.contrib import admin
from .models import Animal, Location, Health_description


@admin.register(Animal)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['name', 'category', 'stock', 'percent', 'initial_price', 'final_price', ]
    # list_editable = ['stock', ]
    pass

@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    pass

@admin.register(Health_description)
class Health_descriptionAdmin(admin.ModelAdmin):
    pass

# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     pass
