from django.shortcuts import render
from devices.models import Device
from django.http import HttpResponse
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from rest_framework.parsers import JSONParser
# from devices.serializers import DeviceSerializer

#def loadDevices(request):
# def devices(request):
#     #return HttpResponse('Hello World!')
#     return render(request,'devices.html')

def device_listing(request):
    """A view of all devices."""
    deviceList = Device.objects.all()
    return render(request, 'devices.html', {'devices': deviceList})
    # return render(request, 'devices.html', {'devices': [{'name': '1'},{'name': '2'},{'name': '3'}]})

"""
Copyright (c) 2019 - present AppSeed.us
"""

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
    

# def deviceAPI(request,id=0):
#     if request.method=="GET":
#         devices = Devices.objects.all()
#         device_serializer = DeviceSerializer(devices,many=true)
#         return JsonResponse(device_serializer.data,safe=False)
#     elif request.method=="POST":
#         device_data = JSONParser().parse(request)
#         device_serializer = DeviceSerializer(data=device_data)
#         if device_serializer.is_valid():
#             device_serializer.save()
#                 return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to add",safe=False)
