from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, Employee_DetailSerializer, DepartmentSerializer, DeptEmpSerializer, DeptManagerSerializer, DeptSuperSerializer, LeaveSerializer, SalarieSerializer
from .models import user, emp_details, department, dept_supervisor, dept_manager, dept_employee, leave, salary
from .models import admin as evtAdmin
from django.core.mail import send_mail
from datetime import datetime
from django.db.models import Count

# serializers
from .serializers import UserSerializer
from .serializers import EventSerializer
from .serializers import AdminSerializer
from .serializers import TicketSerializer, BatchSerializer, Ticket_BatchSerializer
from .serializers import EquipmentSerializer

# models
from .models import user
from .models import admin as evtAdmin
from .models import event
from .models import ticket, batch, batch_ticket
from .models import equipment

# Create your views here.


@api_view(['GET'])
def get_api_url_patterns(request):
    api_urls = {
        'event-all': '/events',
        'users': '/users',


        'EmpDetailList': '/EmployeeDetail-list/',
        'EmpDetailView': '/EmployeeDetail-View/<str:pk>/',
        'EmpDetailCreate': '/EmployeeDetail-Create/',
        'EmpDetailUpdate': '/EmployeeDetail-Update/<str:pk>/',
        'EmpDetailDelete': '/EmployeeDetail-Delete/<str:pk>/',

        'DList': '/department-list/',
        'DView': '/department-View/<str:pk>/',
        'DCreate': '/department-Create/',
        'DUpdate': '/department-Update/<str:pk>/',
        'Ddelete': '/department-Delete/<str:pk>/',
        'DManagDelete': '/deptManager-Delete/<str:pk>/',

        'DManagList': '/deptManager-list/',
        'DManagView': '/deptManager-View/<str:pk>/',
        'DManagCreate': '/deptManager-Create/',
        'DManagUpdate': '/deptManager-Update/<str:pk>/',
        'DManagDelete': '/deptManager-Delete/<str:pk>/',

        'DSuperList': '/deptSupervisor-list/',
        'DSuperView': '/deptSupervisor-View/<str:pk>/',
        'DSuperCreate': '/deptSupervisor-Create/',
        'DSuperUpdate': '/deptSupervisor-Update/<str:pk>/',
        'DSuperDelete': '/deptSupervisor-Delete/<str:pk>/',

        'DEmpList': '/deptEmp-list/',
        'DEmpView': '/deptEmp-View/<str:pk>/',
        'DEmpCreate': '/deptEmp-Create/',
        'DEmpUpdate': '/deptEmp-Update/<str:pk>/',
        'DEmpDelete': '/deptEmp-Delete/<str:pk>/',

        'LeaveList': '/Leave-list/',
        'LeaveView': '/Leave-View/<str:pk>/',
        'LeaveCreate': '/Leave-Create/',
        'LeaveUpdate': '/Leave-Update/<str:pk>/',
        'LeaveDelete': '/Leave-Delete/<str:pk>/',

        'SalaryList': '/Salary-list/',
        'SalaryView': '/Salary-View/<str:pk>/',
        'SalaryCreate': '/Salary-Create/',
        'SalaryUpdate': '/Salary-Update/<str:pk>/',
        'SalaryDelete': '/Salary-Delete/<str:pk>/',

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

# Deepika
# Employee


@api_view(['GET'])
def EmpId(request):
    empidArr = []
    empId = department.objects.all()
    for e in empId:
        empSame = emp_details.objects.filter(
            department__dept_manager_name__emp_det_id__startswith=e)
        for epSame in empSame:
            matchedItem = {
                "username": epSame.employee_name,
                "id": epSame.emp_det_id,
            }
        empidArr.append(matchedItem)

    return Response(empidArr)


@api_view(['GET'])
def deptId(request):
    deptidArr = []
    deptId = dept_manager.objects.all()
    for d in deptId:
        deptSame = department.objects.filter(
            dept_manager__dept_id__dept_id__startswith=d)
        for deptSame in deptSame:
            deptid = {
                "username": deptSame.dept_name,
                "id": deptSame.dept_id
            }
        deptidArr.append(deptid)

    return Response(deptidArr)


@api_view(['GET'])
def EmployeeDetailList(request):
    empdetail = emp_details.objects.all()
    serializer = Employee_DetailSerializer(empdetail, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EmployeeDetailView(request, pk):
    empdetail = emp_details.objects.get(emp_det_id=pk)
    serializer = Employee_DetailSerializer(empdetail, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def EmployeeDetailCreate(request):
    serializer = Employee_DetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['POST'])
def EmployeeDetailsUpdate(request, pk):
    empupdate = emp_details.objects.get(emp_det_id=pk)
    serializer = Employee_DetailSerializer(
        instance=empupdate, data=request.data)


@api_view(['DELETE'])
def EmployeeDetailDelete(request, pk):
    empdetail = emp_details.objects.get(emp_det_id=pk)
    empdetail.delete()

    return Response('Employee Detail succsesfully delete!')


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


@api_view(['PATCH'])
def TicketUpdate(request, pk):
    ticketup = ticket.objects.get(ticket_id=pk)
    serializer = TicketSerializer(
        instance=ticketup, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['GET'])
def TicketListDetail(request, pk):
    ticketdetail = ticket.objects.get(ticket_id=pk)
    serializer = TicketSerializer(ticketdetail, many=False)
    return Response(serializer.data)

# batch


@api_view(['POST'])
def createBatch(request):
    serializer = BatchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def GetBatches(request):
    batches = batch.objects.all()
    serializer = BatchSerializer(batches, many=True)
    return Response(serializer.data)



# batch ticket
@api_view(['POST'])
def createBatchTicket(request):
    serializer = Ticket_BatchSerializer(data=request.data)
    print(serializer.initial_data)
    if serializer.is_valid():
        print(serializer.data)
        batch_ticket.objects.bulk_create(serializer.initial_data)
    return Response(serializer.data)


@api_view(['GET'])
def GetBatchTickets(request):
    batchtickets = batch_ticket.objects.all()
    serializer = Ticket_BatchSerializer(batchtickets, many=True)
    return Response(serializer.data)


# new api ticket
@api_view(['GET'])
def bookingEntries(request):
    tickets = ticket.objects.all()
    array = []
    bid = ''
    btid = ''

    for t in tickets:
        batches = batch.objects.filter(ticket_id=t.ticket_id)
        for b in batches:
            batchticks = batch_ticket.objects.filter(batch_id=b.batch_id)
            for btickets in batchticks:
                obj = {
                    "ticket_id": t.ticket_id,
                    "batch_id": b.batch_id,
                    "batch_ticket_id": btickets.batch_ticket_id,
                    "ticket_name": t.tkt_name,
                    "ticket_price": t.price,
                    "ticket_quantity": t.no_of_tickets
                }

                array.append(obj)
    return Response(array)


# Department

@api_view(['GET'])
def DepartmentList(request):
    departmen = department.objects.all()
    serializer = DepartmentSerializer(departmen, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DepartmentView(request, pk):
    departmen = department.objects.get(dept_id=pk)
    serializer = DepartmentSerializer(departmen, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def DepartmentCreate(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['POST'])
def DepartmentUpdate(request, pk):
    department = department.objects.get(dept_id=pk)
    serializer = Employee_DetailSerializer(
        instance=department, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def DepartmentDelete(request, pk):
    department1 = department.objects.get(dept_id=pk)
    department1.delete()

    return Response('Department succsesfully deleted!')

# MAnager


@api_view(['GET'])
def DepartmentManagerList(request):
    departmentemp = dept_manager.objects.all()
    serializer = DeptManagerSerializer(departmentemp, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DepartmentManagerView(request, pk):
    departmentmanager = dept_manager.objects.get(emp_id=pk)
    serializer = DeptManagerSerializer(departmentmanager, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def DepartmantManagerCreate(request):
    serializer = DeptManagerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def DepartmentManagerUpdate(request, pk):
    departmentmanager = dept_manager.objects.get(emp_id=pk)
    serializer = DeptManagerSerializer(
        instance=departmentmanager, data=request.data)


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
    emailMessage = "An event has been successfully created under the event ID {} by the user registed under the user ID {} in our system. The event creation date is {}. The event details are follows \n\nEvent ID : {}\nEvent Name : {}\nCreated User ID : {}\nEvent Date : {}\nEvent Time : {}\n\n\n\nPS: This is an autogenerated email from CreativeCMB; Please do not reply to this email.".format(
        eventId, user, d4, eventId, eventName, user, date, time)
    send_mail("⚠⚠ DO NOT REPLY ⚠⚠", emailMessage, "mlakilaliyanage@gmail.com", [
              getData["email_address"]], fail_silently=False)
    serializer = EventSerializer(data=getData)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def DepartmentManagerDelete(request, pk):
    departmentmanager = dept_manager.objects.get(emp_id=pk)
    departmentmanager.delete()

    return Response('Manager Detail succsesfully deleted!')

# Supervisor


@api_view(['GET'])
def DepartmentSupervisorList(request):
    departmentsuper = dept_supervisor.objects.all()
    serializer = DeptSuperSerializer(departmentsuper, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DepartmentSupervisorView(request, pk):
    departmentsuper = dept_supervisor.objects.get(emp_id=pk)
    serializer = DeptSuperSerializer(departmentsuper, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def DepartmentSupervisorCreate(request):
    serializer = DeptSuperSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def DepartmentSupervisorUpdate(request, pk):
    departmentsuper = dept_supervisor.objects.get(emp_id=pk)
    serializer = DeptSuperSerializer(
        instance=departmentsuper, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def DepartmentSupervisorDelete(request, pk):
    departmentsuper = dept_supervisor.objects.get(emp_id=pk)
    departmentsuper.delete()

    return Response('Supervisor Detail succsesfully deleted!')

# EmployeeDept


@api_view(['GET'])
def DepartmentEmployeeList(request):
    departmentemp1 = dept_employee.objects.all()
    serializer = DeptEmpSerializer(departmentemp1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DepartmentEmployeeViev(request, pk):
    departmentemp1 = dept_manager.objects.get(emp_id=pk)
    serializer = DeptEmpSerializer(departmentemp1, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def DepartmentEmployeeCreate(request):
    serializer = DeptEmpSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def DepartmentEmployeeUpdate(request, pk):
    departmentemp = dept_employee.objects.get(emp_id=pk)
    serializer = DeptEmpSerializer(instance=departmentemp, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def DepartmentEmployeeDelete(request, pk):
    departmentemp1 = dept_employee.objects.get(emp_id=pk)
    departmentemp1.delete()

    return Response('Employee Detail succsesfully deleted!')

# Leave


@api_view(['GET'])
def LeaveList(request):
    leave1 = leave.objects.all()
    serializer = LeaveSerializer(leave1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def LeaveView(request, pk):
    leave1 = leave.objects.get(leave_id=pk)
    serializer = LeaveSerializer(leave1, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def LeaveCreate(request):
    serializer = LeaveSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def LeaveUpdate(request, pk):
    leave1 = leave.objects.get(leave_id=pk)
    serializer = DeptEmpSerializer(instance=leave1, data=request.data)
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
    serializer = EventSerializer(instance=eventUp, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def LeaveDelete(request, pk):
    leave1 = leave.objects.get(leave_id=pk)
    leave1.delete()

    return Response('Leave Detail succsesfully deleted!')

# Salary


@api_view(['GET'])
def SalarieList(request):
    salary1 = salary.objects.all()
    serializer = SalarieSerializer(salary1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SalarieView(request, pk):
    salary1 = salary.objects.get(sal_id=pk)
    serializer = SalarieSerializer(salary1, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def SalaryCreate(request):
    serializer = SalarieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def SalaryUpdate(request, pk):
    salary1 = salary.objects.get(emp_id=pk)
    serializer = SalarieSerializer(instance=salary1, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)


@api_view(['DELETE'])
def SalaryDelete(request, pk):
    salary1 = salary.objects.get(sal_id=pk)
    salary1.delete()

    return Response('Salary Detail succsesfully deleted!')

# End Deepika


# return the count of events created in the system


@api_view(['GET'])
def EventCount(request):
    eventCount = event.objects.all().count()
    return Response(eventCount)

# return the event count of the logged user


@api_view(['GET'])
def LogUserCount(request, pk):
    logEvent = event.objects.filter(user_id=pk).count()
    return Response(logEvent)

# get the events from the logged user


@api_view(['GET'])
def getLoggedUserEvents(request, pk):
    logEvents = event.objects.all().filter(user_id=pk)
    serializer = EventSerializer(logEvents, many=True)
    return Response(serializer.data)


# return the number of users who has created events in the system
@api_view(['GET'])
def getTotCusEventCount(request):
    cusEventCount = event.objects.values("user_id").distinct().count()
    return Response(cusEventCount)

    # return the number of users who has created events in the system


@api_view(['GET'])
def getEventMonthCount(request):
    # monthCount = event.objects.values("created_month").distinct()
    monthCount = event.objects.values(
        "created_month").order_by("created_month").annotate(count=Count("created_month"))
    return Response(monthCount)
