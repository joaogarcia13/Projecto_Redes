# Import the admin module and your model
from django.contrib import admin
from devices.models import Device

# Página de administração (CRUD dos devices)
# Create a custom admin class
class DeviceAdmin(admin.ModelAdmin):
    # Set the fields to display on the list page
    list_display = ('device_id','name','mac_address','status','type') # display fields on admin

    # Set the fields to be editable on the form page
    fields = ('name','mac_address','status','type') # removed "device_id" field because it's auto-incremented

    # list_filter = ('devices',)

# Register your model with the custom options
admin.site.register(Device, DeviceAdmin)