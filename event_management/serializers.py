from rest_framework import serializers
from .models import user
from .models import event
from .models import admin as evtAdmin
from .models import ticket
from .models import equipment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
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
