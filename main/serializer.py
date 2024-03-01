from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['debt']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['base_price']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = OrderItem
        fields = "__all__"