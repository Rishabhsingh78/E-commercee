from rest_framework import serializers
from .models import *

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product','quantity','price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:

        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'address', 'created_at', 'updated_at','items']
