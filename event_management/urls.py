from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_api_url_patterns),
    path('users/', views.UserList, name="users"),
    path('users/<str:pk>/', views.UserListDetail, name="usersDetails"),
    path('new-user/', views.UserCreate, name="usersCreate"),
    path('user-update/<str:pk>/', views.UserUpdate, name="userUpdate"),
    path('user-delete/<str:pk>/', views.UserDelete, name="userDelete"),

]
