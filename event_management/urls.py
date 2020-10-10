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
    path('events/', views.EventList, name="eventList"),
    # ticket
    path('ticket-create/', views.TicketCreate, name="ticketCreate"),
    path('tickets/', views.GetTickets, name="tickets"),
    path('get-equipments/', views.GetEqForEvent, name="getequipments"),
    path('create-event/', views.EventCreate, name="createevent"),
    path('events/', views.EventGetAll, name="eventgetall"),
    path('events/<str:pk>/', views.EventDetail, name="eventdetail"),
    path('event-delete/<str:pk>/', views.EvenetDelete, name="eventdelete"),
    path('event-update/<str:pk>',views.updateEvent,name="event update"),
    path('ticket-delete/<str:pk>/', views.TicketDelete, name="ticketDelete"),
    path('event-count/', views.EventCount, name="event count"),
    




]
