from django.urls import path

from order.api import views

urlpatterns = [
    path(
        '',
        views.OrderViewSet.as_view({'get': 'orderlist'}),
        name='orderlist'),

    path(
        'orderspruduct/<int:pk>',
        views.OrderViewSet.as_view({'get': 'product'}),
        name='orders_product'),

    path(
        'orderscustomer/<int:pk>',
        views.OrderViewSet.as_view({'get': 'customer'}),
        name='orders_customer'
    ),
]
