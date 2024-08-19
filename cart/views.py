from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['POST'])
def add_cart(request):
    if not request.user.is_authenticated:
        return Response({"error": "User must be authenticated to add items to the cart."}, status=status.HTTP_401_UNAUTHORIZED)

    user = request.user   # user details
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = Cart_Items.objects.get_or_create(cart=cart, product=product)

    # Update the quantity of the cart item
    cart_item.quantity += quantity
    cart_item.save()

    return Response({"message": "Item added to cart."}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_from_cart(request,item_id):


    if not request.user.is_authenticated:
        return Response({"error": "User must be authenticated to remove items from the cart."}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        # Get the user's cart
        cart = Cart.objects.get(user=request.user)
        
        # Find the item in the cart
        cart_item = Cart_Items.objects.get(id=item_id, cart=cart)
        
        # Delete the item from the cart
        cart_item.delete()
        
        return Response({"message": "Item removed from cart."}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
    except Cart_Items.DoesNotExist:
        return Response({"error": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_cart(request, item_id):
    try:
        cart_item = Cart_Items.objects.get(id=item_id, cart__user=request.user)
        quantity = request.data.get('quantity', cart_item.quantity)
        cart_item.quantity = quantity
        cart_item.save()
        return Response(CartItemSerializer(cart_item).data)
    except Cart_Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)