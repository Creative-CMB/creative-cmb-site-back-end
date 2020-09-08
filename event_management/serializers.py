from rest_framework import serializers
from .models import user
from .models import invoice
from .models import payment
from .models import admin as evtAdmin
from .models import advertistment
from .models import package

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
    
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoice 
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = evtAdmin
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = package 
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = advertistment
        fields = '__all__'
