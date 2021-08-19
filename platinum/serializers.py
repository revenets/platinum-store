from rest_framework import serializers
from .models import *


class CartSerializer1(serializers.ModelSerializer):
    oil = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ["oil", "amount"]