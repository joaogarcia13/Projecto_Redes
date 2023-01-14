from rest_framework import serializers
from devices.models import Device, Telemetry, Floor, Device_Floor


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'name', 'ip', 'mac_address', 'wifi_ssid', 'wifi_pwd', 'type', 'status')


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('name', 'image')


class Device_Floor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Device_Floor
        fields = ('idDevice', 'idFloor', 'draw', 'shape')
