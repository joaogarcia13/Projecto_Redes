# Import the admin module and your model
from django.contrib import admin
from devices.models import Device, Floor, Device_Floor


# Página de administração (CRUD dos devices)
# Create a custom admin class
class DeviceAdmin(admin.ModelAdmin):
    # Set the fields to display on the list page
    list_display = ('device_id', 'name', 'ip', 'mac_address', 'wifi_ssid', 'wifi_pwd', 'type', 'coordinates', 'status')  # display fields on admin
    # Set the fields to be editable on the form page
    fields = ('name', 'ip', 'mac_address', 'wifi_ssid', 'wifi_pwd', 'type', 'coordinates', 'status')  # removed "device_id" field because it's auto-incremented


class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    fields = ('name', 'image')


class Device_Floor_Admin(admin.ModelAdmin):
    list_display = ('idDevice', 'idFloor', 'draw', 'shape')
    fields = ('idDevice', 'idFloor', 'draw', 'shape')


# Register your model with the custom options
admin.site.register(Device, DeviceAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Device_Floor, Device_Floor_Admin)
