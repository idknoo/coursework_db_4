from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['name', 'category', 'stock', 'percent', 'initial_price', 'final_price', ]
    # list_editable = ['stock', ]
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'parent_category', ]


# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     pass
