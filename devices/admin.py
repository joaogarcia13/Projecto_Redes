from django.contrib import admin
from devices.models import Device

# Página de administração (CRUD dos devices)

class DeviceAdmin(admin.ModelAdmin):
#    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'devices')
    list_filter = ('devices',)

admin.site.register(Device)  # Use the default options
# admin.site.register(Device, DeviceAdmin)  # Use the customized options
