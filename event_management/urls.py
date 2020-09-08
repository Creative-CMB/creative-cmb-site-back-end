from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_api_url_patterns),
    path('users/', views.UserList, name="users"),
    path('users/<str:pk>/', views.UserListDetail, name="usersDetails"),
    path('new-user/', views.UserCreate, name="usersCreate"),
    path('user-update/<str:pk>/', views.UserUpdate, name="userUpdate"),
    path('user-delete/<str:pk>/', views.UserDelete, name="userDelete"),
    path('admin-list/', views.adminList, name="adminlist"),
    path('payment-list/', views.PaymentList, name="paymentlist"),
    path('invoice-list/', views.InvoiceList, name="InvoiceList"),
    path('invoice/<str:pk>/', views.InvoiceDetails, name="InvoiceDetails"),
    path('invoice-create/', views.InvoiceCreate, name="InvoiceCreate"),
    path('invoice-update/<str:pk>/', views.InvoiceUpdate, name="InvoiceUpdate"),
    path('invoice-delete/<str:pk>/', views.InvoiceDelete, name="InvoiceDelete"),
    path('package-list/', views.PackageList, name="packagelist"),
    path('advertisement-list/', views.AdvertisementList, name="advertisementlist"),
    path('package-create/', views.PackageCreate, name="PackageCreate"),
    path('advertisement-create/', views.AdvertisementCreate, name="AdvertisementCreate"),
    path('package-update/<str:pk>/', views.PackageUpdate, name="PackageUpdate"),
    path('advertisement-update/<str:pk>/', views.AdvertisementUpdate, name="AdvertisementUpdate"),
    path('package-delete/<str:pk>/', views.PackageDelete, name="PackageDelete"),
    path('advertisement-delete/<str:pk>/', views.AdvertisementDelete, name="AdvertisementDelete")





    

    
    

]
