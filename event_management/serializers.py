from rest_framework import serializers
from .models import user,emp_details,department,dept_employee,dept_manager,dept_supervisor,salary,leave
from .models import user
from .models import event
from .models import admin as evtAdmin
from .models import ticket
from .models import equipment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
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

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = leave
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


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment
        fields = "__all__"
