from django.urls import path

from order import views

app_name = 'order'

urlpatterns = [
    path('single_product/', views.single_product, name='single_product'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete_from_cart/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('checkout/', views.checkout, name='checkout')
]
