from rest_framework import serializers
from .models import user,emp_details,department,dept_employee,dept_manager,dept_supervisor,salary
from .models import user
from .models import event
from .models import admin as evtAdmin
from .models import ticket
from .models import equipment, equip_rental, rented_item, inventory_items, rental_details
from .models import ticket,batch_ticket,batch
from .models import equipment
from .models import userActions
import json

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

<<<<<<< HEAD

class InvenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_items
        fields = '__all__'

class RentedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = rented_item
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = equip_rental
        fields = '__all__'


class Rental_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = rental_details
        fields = '__all__'

=======
class ActionSerializer(serializers.Serializer):
    class Meta:
        model = userActions
        fields = "__all__"
>>>>>>> 2729d07bb02ca2944d640ff4525714724cba323a
