from rest_framework import serializers
from devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields=['device_id','name','mac_address','status','type']
