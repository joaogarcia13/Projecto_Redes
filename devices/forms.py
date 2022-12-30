from django import forms

# Not used. Useful for a CRUD page
class DeviceForm(forms.Form):
    #device_id = forms.CharField(label='device_id', max_length=100) # ID editavel (formato de texto)
    # device_id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    ip = forms.CharField(max_length=30)
    mac_address = forms.CharField(max_length=30)
    wifi_ssid = forms.CharField(max_length=100)
    wifi_pwd = forms.CharField(max_length=30)
    type = forms.CharField(max_length=30)
    status = forms.BooleanField(required=False)
