from rest_framework import serializers
from .models import user,emp_details,department,dept_employee,dept_manager,dept_supervisor,salary,leave

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
