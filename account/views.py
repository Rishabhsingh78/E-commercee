from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])

def register(request):
    print("ADFASDFASDfasd")
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User successfully register"},status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['POST'])

def login(request):
    serializer = LoginSerializer(data = request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            refresh_token = RefreshToken.for_user(user)
            return Response({
                'refresh_token': str(refresh_token),
                'access_token': str(refresh_token.access_token),
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({'message':'Invalid email or password'},status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def userlist(request):
    user = User.objects.all()
    serializer = UserSerializer(user,many = True)
    return Response({'Payload':serializer.data},status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message':"successfully logout"},status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        print("Error:", str(e)) 
        return Response({'message':"Token is already blacklist "},status=status.HTTP_400_BAD_REQUEST)