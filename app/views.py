from django.shortcuts import render
from .serializer import UserSerializers
from .models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
# Create your views here.

class UserListApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
    