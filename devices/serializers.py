from rest_framework import serializers
from devices.models import Device, Telemetry, Floor, Device_Floor, QoS_Rules, QoS_Filters, Firewall


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'name', 'ip', 'mac_address', 'wifi_ssid', 'wifi_pwd', 'type', 'coordinates', 'status')


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('name', 'image')


class Device_Floor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Device_Floor
        fields = ('idDevice', 'idFloor', 'draw', 'shape')


class QoS_Rules_Serializer(serializers.ModelSerializer):
    class Meta:
        model = QoS_Rules
        fields = ('id', 'device', 'rule_name', 'max_speed', 'normal_speed')


class QoS_Filters_Serializer(serializers.ModelSerializer):
    class Meta:
        model = QoS_Filters
        fields = ('id', 'device', 'ip', 'rule_name', 'interface', 'priority', 'filterHandle', 'filterType')


class Firewall_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Firewall
        fields = ('id', 'device', 'type', 'port')
