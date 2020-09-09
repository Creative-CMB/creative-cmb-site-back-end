from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import EventSerializer
from .serializers import AdminSerializer
from .serializers import TicketSerializer
from .models import user
from .models import admin as evtAdmin
from .models import event
from .models import ticket
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


@api_view(['GET'])
def EventList(request):
    events = event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def adminList(request):
    adminUserArr = []
    admins = evtAdmin.objects.all()
    for ad in admins:
        users = user.objects.filter(admin__admin_id__user_id__startswith=ad)
        for u in users:
            adminUser = {
                "username": u.first_name,
                "id": u.user_id
            }
        adminUserArr.append(adminUser)

    return Response(adminUserArr)

# Ticket


@api_view(['POST'])
def TicketCreate(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['GET'])
def GetTickets(request):
    tickets = ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def TicketDelete(request, pk):
    tickdel = ticket.objects.get(ticket_id=pk)
    tickdel.delete()
    return Response("deleted")
