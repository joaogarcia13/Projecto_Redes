from django.db import models

class Device(models.Model):
    # device_id = models.CharField(primary_key=True,auto_created=True,max_length=100) # ID em formato de texto
    device_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, null=True)
    ip = models.CharField(max_length=30)
    mac_address = models.CharField(max_length=30)
    wifi_ssid = models.CharField(max_length=100, null=True)
    wifi_pwd = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=30, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Telemetry(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    timestamp = models.CharField(max_length=30)
    data = models.CharField(max_length=500) #pode ser dinamico, então guarda objeto
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE) #chave estrangeira do dispositivo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)