from rest_framework import serializers
from order.models import Order


class OrderslistSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='orders_product',
        lookup_field='pk'
    )
    customer = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='orders_customer',
        lookup_field='pk'
    )

    class Meta:
        model = Order
        fields = '__all__'
