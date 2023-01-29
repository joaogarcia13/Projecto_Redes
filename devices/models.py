from django.db import models


class Device(models.Model):
    # device_id = models.CharField(primary_key=True,auto_created=True,max_length=100) # ID em formato de texto
    device_id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    ip = models.CharField(max_length=30)
    mac_address = models.CharField(max_length=30)
    wifi_ssid = models.CharField(max_length=100, null=True)
    wifi_pwd = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=30, null=True)
    coordinates = models.CharField(max_length=30, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Telemetry(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)  # chave estrangeira do dispositivo
    timestamp = models.CharField(max_length=30)
    data = models.CharField(max_length=250)  # pode ser dinamico, então guarda objeto
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Floor(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='devices/static/assets/img/floors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Device_Floor(models.Model):
    idDevice = models.ForeignKey(Floor, on_delete=models.CASCADE)  # chave estrangeira do dispositivo
    idFloor = models.ForeignKey(Device, on_delete=models.CASCADE)  # chave estrangeira do edificio
    draw = models.CharField(max_length=250)
    shape = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QoS_Rules(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    # name = models.CharField(max_length=250) # nome da regra é para ser legivel ao cliente
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  # chave estrangeira do dispositivo
    rule_name = models.CharField(max_length=100)
    max_speed = models.CharField(max_length=100)
    normal_speed = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QoS_Filters(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    rule = models.ForeignKey(QoS_Rules, on_delete=models.CASCADE)  # chave estrangeira da regra
    ip = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Firewall(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  # chave estrangeira do dispositivo
    type = models.CharField(max_length=250)
    port = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
