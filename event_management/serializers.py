from rest_framework import serializers
from .models import user,emp_details,department,dept_employee,dept_manager,dept_supervisor,salary
from .models import user
from .models import event
from .models import admin as evtAdmin
from .models import ticket,batch_ticket,batch, reservation
from .models import equipment
<<<<<<< HEAD
from .models import userActions
import json
from django.contrib.auth.models import User
=======
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import userActions
import json

>>>>>>> a4fc304e361eed37d54319c95ea8f98268f94572

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class LoggedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Employee_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = emp_details
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'

class DeptManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = dept_manager
        fields = '__all__'

class DeptSuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = dept_supervisor
        fields = '__all__'

class DeptEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = dept_employee
        fields = '__all__'

class SalarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = salary
        fields = '__all__'
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = evtAdmin
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = "__all__"

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = batch
        fields = "__all__"


class Ticket_BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = batch_ticket
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = "__all__"
class ActionSerializer(serializers.Serializer):
    class Meta:
        model = userActions
        fields = "__all__"
