from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import InvoiceSerializer
from .serializers import PaymentSerializer
from .serializers import AdminSerializer
from .serializers import PackageSerializer
from .serializers import AdvertisementSerializer
from .models import invoice
from .models import user
from .models import admin as evtAdmin
from .models import payment
from .models import package
from .models import advertistment

# Create your views here.


@api_view(['GET'])
def get_api_url_patterns(request):
    api_urls = {
        'event-all' : '/events',
        'users': '/users',
        'payment' :'/payment-list',
        'admins' :'/admin-list'
        
    }

    return Response(api_urls)

@api_view(['GET'])
def PaymentList(request):
    payments=payment.objects.all()
    serializer=  PaymentSerializer(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def adminList(request):
    adminUserArr=[]
    admins = evtAdmin.objects.all()
    for ad in admins:
        users = user.objects.filter(admin__admin_id__user__user_id=ad)
        for u in users:
            adminUser = {
                "username":u.first_name,
                "id":u.user_id
            }
        adminUserArr.append(adminUser)
    
    return Response(adminUser)

@api_view(['GET'])
def UserList(request):
    users = user.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def UserListDetail(request,pk):
    users = user.objects.get(user_id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['POST'])
def UserUpdate(request, pk):
    users = user.objects.get(user_id=pk)
    serializer = UserSerializer(instance=users,data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def UserDelete(request, pk):
    users = user.objects.get(user_id=pk)
    users.delete()
    return Response("deleted")

@api_view(['GET'])
def PackageList(request):
    packages = package.objects.all()
    serializer = PackageSerializer(packages,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AdvertisementList(request):
    advertistments= advertistment.objects.all()
    serializer = AdvertisementSerializer(advertistments,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def InvoiceList(request):
    invoices = invoice.objects.all()
    serializer = InvoiceSerializer(invoices,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def InvoiceDetails(request,pk):
    invoices = invoice.objects.get(invoice_id=True)
    serializer = InvoiceSerializer(invoices,many=True)


@api_view(['POST'])
def InvoiceCreate(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)

@api_view(['POST'])
def PackageCreate(request):
    serializer = PackageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
       
    return Response(serializer.data)

@api_view(['POST'])
def AdvertisementCreate(request):
    serializer = AdvertisementSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
       
    return Response(serializer.data)

@api_view(['POST'])
def InvoiceUpdate(request,pk):
    invoices = invoice.objects.get(invoice_id=pk)
    serializer = InvoiceSerializer(instance=invoices, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def PackageUpdate(request,pk):
    packages = package.objects.get(pack_id=pk)
    serializer = PackageSerializer(instance=packages, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def AdvertisementUpdate(request,pk):
    advertisements = advertistment.objects.get(ad_id=pk)
    serializer = AdvertisementSerializer(instance=advertistments, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)



@api_view(['DELETE'])
def InvoiceDelete(request,pk):
    invoices = invoice.objects.get(invoice_id=pk)
    invoices.delete()

    return Response('Invoice successfully deleted')

@api_view(['DELETE'])
def PackageDelete(request,pk):
    packages = package.objects.get(pack_id=pk)
    packages.delete()

    return Response('Package successfully deleted')

@api_view(['DELETE'])
def AdvertisementDelete(request,pk):
    advertisements = advertistment.objects.get(ad_id=pk)
    advertisements.delete()

    return Response('advertisments successfully deleted')


