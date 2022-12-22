from rest_framework import serializers
from account.models import Account


class RegisterationSerialiser(serializers.ModelSerializer):

    style = {'input_type': 'password'}
    password2 = serializers.CharField(style=style, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2', ]