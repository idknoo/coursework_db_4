from django.contrib import admin
from order.models import Order, OrderItem, Work_shedule


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
     list_editable  = ['status']
     list_display =['id', 'animals', 'customer', 'status']
     def animals(self, obj):
         return "\n".join(["'" + str(p.product) + "'" for p in obj.order_item.all()])


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(OrderItem)


@admin.register(Work_shedule)
class Work_sheduleAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Work_shedule)
