from django.contrib import admin
from order.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
    # list_display = ['customer', 'product', 'stock', 'availability', ]
    # list_filter = ['customer']
    # list_editable = ['stock', 'availability', ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
