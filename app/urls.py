from django.urls import path, re_path
from .views import UserListApiView

urlpatterns = [
    path('api/',UserListApiView.as_view())
]