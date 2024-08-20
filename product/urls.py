from django.urls import path
from .views import *


urlpatterns = [
    path('add-product/', add_product, name='add_product'),
    path('view-product/',view_product,name = 'view_product'),
    path('edit-product/<int:pk>/',edit_product,name = 'edit_product'),
    path('search/', product_search, name='product_search')
]