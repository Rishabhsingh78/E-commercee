from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cart.models import *
from . serializers import *
from .models import *
from decimal import Decimal
@api_view(['POST'])
def place_order(request):
    if not request.user.is_authenticated:
        return Response({"error": "User must be authenticated to place an order."}, status=status.HTTP_401_UNAUTHORIZED)

    user = request.user
    address = request.data.get('address')
    if not address:
        return Response({"error": "Address is required to place an order."}, status=status.HTTP_400_BAD_REQUEST)

    # Calculate total_price based on cart items (this is just a placeholder)
    total_price = Decimal(0) 
    cart = Cart.objects.get(user=user)
    for item in cart.items.all():
        total_price += item.product.price * item.quantity

    order = Order.objects.create(user=user,total_price= total_price, address=address)
    
    # Clear the cart after order is placed (if required)
    cart.items.all().delete()

    return Response({"message": "Order placed successfully.", "order_id": order.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def view_order(request):
    if not request.user.is_authenticated:
        return Response({'error':'User must be authenticated to place an order'},status=status.HTTP_401_UNAUTHORIZED)
    user = request.user
    orders = Order.objects.filter(user= user)
    serializer = OrderSerializer(orders,many = True)
    return Response({'payload': serializer.data},status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_order(request,order_id):
    if  not request.user.is_authenticated:
        return Response({"error":"User must be authenticated to update an order."},status=status.HTTP_400_BAD_REQUEST)
    user = request.user
    try:
        order = Order.objects.get(id = order_id,user= user)
    except Order.DoesNotExist:
        return Response({'message':'User does not exits'},status=status.HTTP_404_NOT_FOUND)
    
    if 'status' in request.data:
        order.status = request.data['status']
        order.save()

    return Response({"message": "Order updated successfully."}, status=status.HTTP_200_OK)