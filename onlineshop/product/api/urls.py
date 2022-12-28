from django.urls import path

from product.api import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductAPIView.as_view()),
    path('<str:category>/', views.ProductAPIView.as_view()),
]
