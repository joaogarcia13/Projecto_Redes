from rest_framework import serializers
from devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields=('device_id','name','ip','mac_address','wifi_ssid','wifi_pwd','type','status')
