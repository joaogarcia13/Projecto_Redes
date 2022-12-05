from rest_framework import serializers
from devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields=('id','name','mac_address')
