from rest_framework import serializers
from .models import user,emp_details,department,dept_employee,dept_manager,dept_supervisor,salary
from .models import user
from .models import event
from .models import admin as evtAdmin
from .models import ticket,batch_ticket,batch, reservation
from .models import equipment
<<<<<<< HEAD
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
=======
from .models import userActions
import json
>>>>>>> 98db430d7eed5871b37554722933dad5630d7b8d


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user    



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
