from django.db import models

class Device(models.Model):
    # device_id = models.CharField(primary_key=True,auto_created=True,max_length=100) # ID em formato de texto
    device_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)