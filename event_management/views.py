from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import EventSerializer
from .serializers import AdminSerializer
from .models import user
from .models import event
from .models import admin as evtAdmin

# Create your views here.


@api_view(['GET'])
def get_api_url_patterns(request):
    api_urls = {
        'event-all': '/events',
        'users': '/users',
    }

    return Response(api_urls)


@api_view(['GET'])
def UserList(request):
    users = user.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def UserListDetail(request, pk):
    users = user.objects.get(user_id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['POST'])
def UserUpdate(request, pk):
    users = user.objects.get(user_id=pk)
    serializer = UserSerializer(instance=users, data=request.data)
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

# get method to fetch all objects from database and return


@api_view(['GET'])
def EventList(request):
    events = event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AdminList(request):
    userArr = []
    admins = evtAdmin.objects.all()
    for ad in admins:
        usrad = user.objects.filter(user_id=ad)
        username = usrad.first_name
        userid = ad
        tempUsr = {
            "usrname": username,
            "usrid": userid
        }

        userArr.append(tempUsr)

    #serializer = AdminSerializer(admins, many=True)
    return Response(userArr)
