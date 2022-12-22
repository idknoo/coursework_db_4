from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
