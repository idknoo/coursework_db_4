from rest_framework import serializers
from product.models import Animal


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(
        source='category.category_name',
        read_only=True,
    )
    final_price = serializers.ReadOnlyField(
        source='generate_final_price'
    )

    class Meta:
        model = Animal
        fields = '__all__'

