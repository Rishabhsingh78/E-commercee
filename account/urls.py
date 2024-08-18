from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('userlist/',userlist,name= 'userlist'),
    path('logout/', logout, name='logout'),
]