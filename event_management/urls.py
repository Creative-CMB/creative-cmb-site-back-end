from django.urls import path
from . import views
from rest_framework import routers 
from django.conf.urls import include


urlpatterns = [
     path('api/', views.get_api_url_patterns),
     path('users/', views.UserList, name="users"),
     path('users/<str:pk>/', views.UserListDetail, name="usersDetails"),
     path('new-user/', views.UserCreate, name="usersCreate"),
     path('user-update/<str:pk>/', views.UserUpdate, name="userUpdate"),
     path('user-delete/<str:pk>/', views.UserDelete, name="userDelete"),
     path('loggedusers/', views.LoggedUserList, name="loggedUsers"),
     path('loggeduser-delete/<str:pk>/', views.LoggedUserDelete, name="loggedUserDelete"),
     path('dashboard/', views.dashboard, name="dashboard"),
	path('registeradmin/', views.registerAdminPage, name="registeradmin"),     
	path('signin/', views.signinPage, name="signin"),
	path('login/', views.loginPage, name="login"),	
	path('logout/', views.logoutUser, name="logout"),
     path('admin-list/', views.adminList, name="adminlist"),
     path('events/', views.EventList, name="eventList"),


     # ticket
     path('ticket-create/', views.TicketCreate, name="ticketCreate"),
     path('tickets/', views.GetTickets, name="tickets"),
     path('ticket-delete/<str:pk>/', views.TicketDelete, name="ticketDelete"),
     path('ticket-update/<str:pk>/', views.TicketUpdate, name="ticketUpdate"),
     path('ticket-detail/<str:pk>/', views.TicketListDetail, name="ticketDetails"),

     # batch
     path('batch-create/', views.createBatch, name="batchCreate"),
     path('batches/', views.GetBatches, name="batches"),

     # batch ticket
     path('batchTicket-create/', views.createBatchTicket, name="batchTicketCreate"),
     path('batchTickets/', views.GetBatchTickets, name="batchTickets"),

     # reservation
     path('create-res/', views.ReservationCreate, name="createReservation"),
     path('resTicket-list/', views.GetReserveTickets, name="reservationDetails"),
     path('reservation-by-id/<str:id>/', views.GetReservationByID, name="reservationbyid"),
     # booking
     path('displayentries/', views.bookingEntries, name='booking'),



     path('get-equipments/', views.GetEqForEvent, name="getequipments"),
     path('create-event/', views.EventCreate, name="createevent"),
     path('events/', views.EventGetAll, name="eventgetall"),
     path('events/<str:pk>/', views.EventDetail, name="eventdetail"),
     path('event-delete/<str:pk>/', views.EvenetDelete, name="eventdelete"),
     path('event-update/<str:pk>', views.updateEvent, name="event update"),
     #path('ticket-delete/<str:pk>/', views.TicketDelete, name="ticketDelete"),
     path('event-count/', views.EventCount, name="event count"),
     path('event-count/<str:pk>', views.LogUserCount,
          name="event count of logged users"),
     path('my-events/<str:pk>/', views.getLoggedUserEvents,
          name="event of logged user"),
     path('event-user-count/', views.getTotCusEventCount, name="event user count"),
     path('event-month-count/', views.getEventMonthCount, name="event month count"),
     path('actions/', views.userActions, name="actions"),
     path('event-status/<str:pk>/', views.EventStatusUpdate,
          name="update the status of the event"),





     path('admin-list/', views.adminList, name="adminlist"),

     # Employee Details
     path('EmployeeDetail-list/', views.EmployeeDetailList,
          name="EmployeeDetail-list"),
     path('EmployeeDetail-View/<str:pk>/',
          views.EmployeeDetailView, name="EmployeeDetail-View"),
     path('EmployeeDetail-Create/', views.EmployeeDetailCreate,
          name="EmployeeDetail-Create"),
     path('EmployeeDetail-Delete/<str:pk>/',
          views.EmployeeDetailDelete, name="EmployeeDetail-Delete"),
     path('EmployeeDetail-Update/<str:pk>/',
          views.EmployeeDetailsUpdate, name="EmployeeDetail-update"),
     path('Employeeid/', views.EmpId, name="Employeeid"),
     path('Deptid/', views.deptId, name="deptid"),
     path('EmployeeDetail-list/', views.EmployeePDF, name="EmployeeDetail-list"),


     # Department
     path('department-list/', views.DepartmentList, name="department-list"),
     path('department-View/<str:pk>/',
          views.DepartmentView, name="department-View"),
     path('department-Create/', views.DepartmentCreate, name="department-Create"),
     path('department-Update/<str:pk>/',
          views.DepartmentUpdate, name="department-Update"),
     path('department-Delete/<str:pk>/',
          views.DepartmentDelete, name="department-Delete"),
          path('department-list/', views.DepartmentPDF, name="department-list"),

     # Department Manager
     path('deptManager-list/', views.DepartmentManagerList, name="deptManager-list"),
     path('deptManager-View/<str:pk>/',
          views.DepartmentManagerView, name="deptManager-View"),
     path('deptManager-Create/', views.DepartmantManagerCreate,
          name="deptManager-Create"),
     path('deptManager-Update/<str:pk>/',
          views.DepartmentManagerUpdate, name="deptManager-Update"),
     path('deptManager-Delete/<str:pk>/',
          views.DepartmentManagerDelete, name="deptManager-Delete"),
          path('deptManager-list/', views.DeptManagerPDF, name="deptManager-list"),


     # Department Supervisor
     path('deptSupervisor-list/', views.DepartmentSupervisorList,
          name="deptSupervisor-list"),
     path('deptSupervisor-View/<str:pk>/',
          views.DepartmentSupervisorView, name="deptSupervisor-View"),
     path('deptSupervisor-Create/', views.DepartmentSupervisorCreate,
          name="deptSupervisor-Create"),
     path('deptSupervisor-Update/<str:pk>/',
          views.DepartmentSupervisorUpdate, name="deptSupervisor-Update"),
     path('deptSupervisor-Delete/<str:pk>/',
          views.DepartmentSupervisorDelete, name="deptSupervisor-Delete"),


     # Department Employee
     path('deptEmp-list/', views.DepartmentEmployeeList, name="deptEmp-list"),
     path('deptEmp-View/<str:pk>/',
          views.DepartmentEmployeeViev, name="deptEmp-View"),
     path('deptEmp-Create/', views.DepartmentEmployeeCreate,
          name="deptEmp-Create"),
     path('deptEmp-Update/<str:pk>/',
          views.DepartmentEmployeeUpdate, name="deptEmp-Update"),
     path('deptEmp-Delete/<str:pk>/',
          views.DepartmentEmployeeDelete, name="deptEmp-Delete"),


     # Salary
     path('Salary-list/', views.SalarieList, name="Salary-list"),
     path('Salary-View/<str:pk>/', views.SalarieView, name="Salary-View"),
     path('Salary-Create/', views.SalaryCreate, name="Salary-Create"),
     path('Salary-Update/<str:pk>/', views.SalaryUpdate, name="Salary-Update"),
     path('Salary-Delete/<str:pk>/', views.SalaryDelete, name="Salary-Delete"),
     path('Salary-list/', views.SalaryPDF, name="Salary-list"),

]
