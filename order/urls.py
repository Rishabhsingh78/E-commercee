from django.urls import path
from . views import *

urlpatterns = [
    path('place-order/', place_order, name='place_order'),
    path('view-order/', view_order, name='place_order'),
    path('update-order/<int:order_id>/', update_order, name='place_order'),
]
