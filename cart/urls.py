from django.urls import path
from . views import *

urlpatterns = [
    path('add-cart/', add_cart, name='add_to_cart'),
    path('delete-cart/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
    path('update-cart/<int:item_id>/', update_cart, name='update_cart'),
    path('view-cart/', view_cart, name='view_cart'),
]