from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

from customer.models import Customer
from order.api.serializer import OrderslistSerializer
from order.models import Order
from product.models import Product


class OrderViewSet(viewsets.ViewSet):
    def orderlist(self, request):
        queryset = get_list_or_404(Order)
        serializer = OrderslistSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def product(self, request, pk):
        queryset = get_list_or_404(Product, id=pk)
        serializer = OrderslistSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def customer(self, request, pk):
        queryset = get_list_or_404(Customer, id=pk)
        serializer = OrderslistSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
