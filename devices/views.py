import json
import requests

from django.shortcuts import render
from django import template
from django.template import loader
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse

from devices.models import Device, Telemetry, Floor, Device_Floor, QoS_Rules, QoS_Filters, Firewall
from devices.forms import DeviceForm
from devices.serializers import DeviceSerializer, Device_Floor_Serializer, QoS_Rules_Serializer, QoS_Filters_Serializer, Firewall_Serializer
from django.core.files import File
from django.core.files.storage import default_storage

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

"""
Copyright (c) 2019 - present AppSeed.us
"""


# --- PAGES
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    logout(request)
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # authentication_classes = [SessionAuthentication, BasicAuthentication]
        # permission_classes = [IsAuthenticated]
        # print('is Auth?: '+permission_classes[0])
        # token = Token.objects.create(user=...)
        # print('TOKEN'+token.key)

        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect('/')
                if (request.POST['next'] == None):
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect(request.POST['next'])

    return render(request, 'home/login.html', )


@login_required(login_url='/login')
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')

    if request.user.is_superuser:
        deviceList = Device.objects.all()
    else:
        deviceList = Device.objects.all().filter(status=1)

    # return HttpResponse(html_template.render(context, request))
    return render(request, 'home/index.html', {'devices': deviceList})


@login_required(login_url='/login')
def device_details(request, id):
    device = Device.objects.get(device_id=id)
    qos_rules = QoS_Rules.objects.all().filter(device=id)
    # qos_filters = QoS_Filters.objects.all().filter(rule=qos_rules.id)

    # for rule in qos_rules:
    #     print(rule.id)

    obj_render = {
        'device': device,
        'qos_rules': qos_rules,
        # 'qos_filters': qos_filters
    }

    return render(request, 'home/device_details.html', obj_render)


@login_required(login_url='/login')
def map(request):
    floors = Floor.objects.all()
    return render(request, 'home/map.html', {'floors': floors})


@login_required(login_url='/login')
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        print("PAGES -> " + load_template)

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template + '.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


# AUTH
# --- DEVICE API
@api_view(['GET'])
def getDevice(request):
    try:
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        print('user' + str(request.user))
        print('auth' + str(request.auth))

        devices = Device.objects.all()
        device_serializer = DeviceSerializer(devices, many=True)
        return JsonResponse(device_serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=400)


@api_view(['POST'])
def setDevice(request):
    try:
        device_data = JSONParser().parse(request)
        device_serializer = DeviceSerializer(data=device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['PUT'])
def updateDevice(request, id):
    device = Device.objects.get(device_id=id)
    devices_serializer = DeviceSerializer(device, data=request.data)

    if devices_serializer.is_valid():
        devices_serializer.save()
        return JsonResponse("Updated Successfully", safe=False)
    else:
        return JsonResponse("Failed to Update", safe=False)


@api_view(['DELETE'])
def deleteDevice(request, id):
    device = Device.objects.get(device_id=id)
    device.delete()
    return JsonResponse("Deleted Successfully", safe=False)


@login_required(login_url='/login')
def formDevice(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeviceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            ip = form.cleaned_data['ip']
            mac_address = form.cleaned_data['mac_address']
            wifi_ssid = form.cleaned_data['wifi_ssid']
            wifi_pwd = form.cleaned_data['wifi_pwd']
            type = form.cleaned_data['type']
            status = form.cleaned_data['status']

            print(f'{name},{ip},{mac_address},{wifi_ssid},{wifi_pwd},{type},{status}')
            # create json object
            obj = {
                'name': name,
                'ip': ip,
                'mac_address': mac_address,
                'wifi_ssid': wifi_ssid,
                'wifi_pwd': wifi_pwd,
                'type': type,
                'status': status
            }
            jsonList = json.dumps(obj, separators=(',', ':'))
            print(jsonList)

            # add device to database
            requests.post(f'http://127.0.0.1:8000/api/devices/new', data=jsonList)

            # redirect to a new URL:
            return HttpResponseRedirect('/devices')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeviceForm()

    return render(request, 'home/device/new.html', {'form': form})


@api_view(['GET'])
def drawDevices(request):
    try:
        coords = Device_Floor.objects.all()
        print('coordinates' + str(coords))

        device_floor_serializer = Device_Floor_Serializer(coords, many=True)
        return JsonResponse(device_floor_serializer.data, safe=False)
    except Exception as e:
        return JsonResponse("Error: " + str(e), safe=False)


# EXTERNAL API
@api_view(['GET'])
def external_api_toggle_switch(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    switch_command = request.GET["data"]
    obj = {"action": switch_command}
    try:
        req = requests.post(f'http://{device_ip}:5000/toggleSwitch', data=obj)
        if req.status_code == 200:
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + req.text)
            return JsonResponse({"data": "Switch set", "status": req.status_code}, safe=False)
        else:
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['POST'])
def external_api_create_wifi(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    object = {
        'name': request.POST["wifi_ssid"],
        'password': request.POST["wifi_pwd"]
    }

    try:
        req = requests.post(f'http://{device_ip}:5000/createwifi', data=object)
        print(req.status_code)

        if req.status_code == 200:
            data = req.text
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + data)
            return JsonResponse({"data": "Created Successfully", "status": req.status_code}, safe=False)
        else:
            print("Error: " + "Request failed")
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['POST'])
def external_api_set_ip(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    payload = {
        'ip': request.POST.get("ip"),
        'subnet': request.POST.get("subnet"),
        'range1': request.POST.get("range1"),
        'range2': request.POST.get("range2"),
        'dns': request.POST.get("dns"),
    }
    print(payload)

    # jsonList = json.dumps(payload, separators=(',', ':'))

    try:
        req = requests.post(f'http://{device_ip}:5000/setip', data=payload)

        if req.status_code == 200:
            telemetries = req.text
            print('Status: ' + str(req) + ' IP: ' + device_ip)
            return JsonResponse({"data": "IP set", "status": req.status_code}, safe=False)
        else:
            print("Error: " + "Request failed")
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['GET'])
def external_api_kill_network(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    try:
        req = requests.get(f'http://{device_ip}:5000/killnetwork', timeout=3)

        if req.status_code == 200:
            resp = req.text
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + resp)
            return JsonResponse(resp)
        else:
            print("Error: " + "Request failed")
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['GET'])
def external_api_get_info(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    try:
        req = requests.get(f'http://{device_ip}:5000/getinfo', timeout=3)

        if req.status_code == 200:
            telemetries = req.text
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA:' + telemetries)
            return JsonResponse({"data": telemetries, "status": req.status_code})
        else:
            print("Error: " + "Request failed")
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['POST'])
def external_api_add_qos_rule(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    qos_rule_name = request.POST["name"]
    qos_rule_max_speed = request.POST["max_speed"]
    qos_rule_normal_speed = request.POST["normal_speed"]
    obj = {
        "name": qos_rule_name,
        "velocidadeLimitada": qos_rule_max_speed,
        "velocidadeNormal": qos_rule_normal_speed
    }

    try:
        req = requests.post(f'http://{device_ip}:5000/criarRegraQoS', data=obj)

        if req.status_code == 200:
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + req.text)

            add_qos = {
                "rule_name": qos_rule_name,
                "device": device.device_id,
                "max_speed": qos_rule_max_speed,
                "normal_speed": qos_rule_normal_speed
            }
            # add QoS to database
            added_qos = add_qos_rule_db(add_qos)
            if added_qos.status_code == 200:
                return JsonResponse({"data": "QoS Rule created + Added to Database", "status": req.status_code}, safe=False)

            return JsonResponse({"data": "QoS Rule created", "status": req.status_code}, safe=False)
        else:
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)
@api_view(['POST'])
def external_api_remove_qos_rule(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    qos_rule_id = request.POST["rule_id"]
    qos_rule_name = request.POST["name"]
    obj = {
        "name": qos_rule_name
    }

    try:
        req = requests.post(f'http://{device_ip}:5000/apagarRegraQoS', data=obj)
        if req.status_code == 200:
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + req.text)

            # add QoS to database
            removed_qos = remove_qos_rule_db(qos_rule_id)
            if removed_qos != 200:
                return JsonResponse({"data": "Failed to delete from database", "status": req.status_code}, safe=False)

            return JsonResponse({"data": "QoS Rule deleted", "status": req.status_code}, safe=False)
        else:
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['POST'])
def external_api_add_qos_filter(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    qos_filter_ip = request.POST["ip"]
    qos_filter_rule_name = request.POST["rule_name"]
    obj = {
        "ip": qos_filter_ip,
        "nomeRegra": qos_filter_rule_name,
    }

    try:
        req = requests.post(f'http://{device_ip}:5000/criarFiltroQoS', data=obj)
        if req.status_code == 200:
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + req.text)
            # TODO: ADD TO DATABASE
            return JsonResponse({"data": "QoS Filter created", "status": req.status_code}, safe=False)
        else:
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


@api_view(['POST'])
def external_api_add_firewall_rule(request, id):
    device = Device.objects.get(device_id=id)
    device_ip = device.ip

    firewall_type = request.POST["type"]
    firewall_port = request.POST["port"]
    obj = {
        "tipo": firewall_type,
        "ipPort": firewall_port,
    }

    try:
        req = requests.post(f'http://{device_ip}:5000/criarRegraFirewall', data=obj)
        if req.status_code == 200:
            print('Status: ' + str(req) + ' IP: ' + device_ip + ' DATA: ' + req.text)
            # TODO: ADD TO DATABASE
            return JsonResponse({"data": "Firewall Rule created", "status": req.status_code}, safe=False)
        else:
            return JsonResponse({"data": "Request failed", "status": req.status_code}, safe=False)
    except Exception as e:
        print(f'Unable to connect to {device_ip}')
        return JsonResponse({"data": "Unable to connect to " + device_ip, "status": str(e)}, safe=False)


# RULES to DB
def add_qos_rule_db(qos_data): # ADD QoS rule to database
    try:
        print('ADDED TO DB -> ' + str(qos_data))
        qos_serializer = QoS_Rules_Serializer(data=qos_data)
        if qos_serializer.is_valid():
            qos_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
def remove_qos_rule_db(id):  # DELETE QoS rule from database
    qos_rules = QoS_Rules.objects.get(id=id)
    qos_rules.delete()
    return JsonResponse("Deleted Successfully", safe=False)


def add_qos_filter_db(request): # add QoS to database
    qos_data = JSONParser().parse(request)
    qos_serializer = QoS_Filters_Serializer(data=qos_data)
    if qos_serializer.is_valid():
        qos_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    else:
        return JsonResponse("Failed to add", safe=False)
def add_firewall_rule_db(request): # add QoS to database
    firewall_data = JSONParser().parse(request)
    firewall_serializer = Firewall_Serializer(data=firewall_data)
    if firewall_serializer.is_valid():
        firewall_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    else:
        return JsonResponse("Failed to add", safe=False)


@api_view(['GET'])
def getQoSRules(request, id):
    try:
        rules = QoS_Rules.objects.get(id=id)
        qos_serializer = QoS_Rules_Serializer(rules, many=True)
        print(qos_serializer.data)
        return JsonResponse(qos_serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=400)


def createGraph(request, id):
    telemetries = Telemetry.objects.get(device_id=id)
    print(telemetries)
    device_ip = telemetries.device_id.ip
    print(device_ip)
    req = requests.get(f'http://{device_ip}:5000/')

    if req.status_code == 200:
        print('Status: ' + str(req) + ' IP: ' + device_ip)

    return render(request, 'home/device_details.html', {'data': telemetries})
