from rest_framework import serializers
from .models import *
from product.serializers import *

class CartItemSerializer(serializers.ModelSerializer): # iska mtlb hai ki cart m kitne items hai aur kunsse product hai
    product = ProductSerializer() # yaha product k serializer honge
    class Meta:
        model = Cart_Items
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):  # iske andar jate hi hme jasise cart hota waisa kam hoga
    items = CartItemSerializer(many = True,read_only = True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']