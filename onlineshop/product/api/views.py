from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from product.api.serializer import ProductsListSerializer
from product.models import Animal


class ProductAPIView(APIView):
    serializer = ProductsListSerializer

    def get_queryset(self):
        return Animal.objects.all()

    def get(self, request, category=None):
        if category:
            queryset = get_list_or_404(Animal, category__category_name=category)
        else:
            queryset = self.get_queryset()

        serializer = ProductsListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

