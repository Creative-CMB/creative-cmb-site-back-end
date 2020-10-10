from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from datetime import datetime

# serializers
from .serializers import UserSerializer
from .serializers import EventSerializer
from .serializers import AdminSerializer
from .serializers import TicketSerializer
from .serializers import EquipmentSerializer

# models
from .models import user
from .models import admin as evtAdmin
from .models import event
from .models import ticket
from .models import equipment

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

# fetch the equpiments fro the create event (himasha oya wenama ekak hadanna)


@api_view(['GET'])
def GetEqForEvent(request):
    eqEv = equipment.objects.all()
    serializer = EquipmentSerializer(eqEv, many=True)
    return Response(serializer.data)


# event create view
@api_view(['POST'])
def EventCreate(request):
    getData = request.data
    # print(getData["event_id"])
    eventId = getData["event_id"]
    user = getData["user_id"]
    eventName = getData["event_name"]
    date = getData["date"]
    time = getData["time"]
    d4 = datetime.today().strftime('%Y-%m-%d')
    emailMessage = "An event has been successfully created under the event ID {} by the user registed under the user ID {} in our system. The event creation date is {}. The event detais are follows \nEvent ID : {}\nEvent Name : {}\nCreated User ID : {}\nEvent Date : {}\nEvent Time : {}".format(eventId, user, d4, eventId, eventName, user, date, time)
    send_mail("Do not reply",emailMessage,"mlakilaliyanage@gmail.com",["mlakilaliyanage@hotmail.com"],fail_silently=False)
    serializer = EventSerializer(data=getData)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)

# fetch and terurn all the events in the db


@api_view(['GET'])
def EventGetAll(request):
    events = event.objects.all()
    serializer = EquipmentSerializer(events, many=True)
    return Response(serializer.data)

# fetch a exact event


@api_view(['GET'])
def EventDetail(request, pk):
    eventDet = event.objects.get(event_id=pk)
    serializer = EventSerializer(eventDet, many=False)
    return Response(serializer.data)

# delete the event


@api_view(['DELETE'])
def EvenetDelete(request, pk):
    eventDel = event.objects.get(event_id=pk)
    eventDel.delete()

    return Response(200)

# event update view
@api_view(['POST'])
def updateEvent(request, pk):
    eventUp = event.objects.get(event_id=pk)
    serializer = EventSerializer(instance=eventUp,data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def TicketDelete(request, pk):
    tickdel = ticket.objects.get(ticket_id=pk)
    tickdel.delete()
    return Response("deleted")

#return the count of events created in the system


@api_view(['GET'])
def EventCount(request):
    eventCount = event.objects.all().count()
    return Response(eventCount)

