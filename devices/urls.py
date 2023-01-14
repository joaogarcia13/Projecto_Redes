from django.urls import path, re_path, include
from . import views

# URL Configs
urlpatterns = [
    # The home page
    path('', views.index, name='index'),
    path('devices', views.index, name='home'),
    path('devices/new', views.formDevice),
    path('devices/<int:id>', views.device_details),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('map', views.map, name='map'),
    path('register', views.pages, name='register'),

    # API
    path('api/devices', views.getDevice),
    path('api/devices/new', views.setDevice),
    path('api/devices/<int:id>/update', views.updateDevice),
    path('api/devices/<int:id>/delete', views.deleteDevice),
    path('api/devices/polygons', views.drawDevices),

    # External API
    path("devices/external/toggle_switch/<int:id>", views.external_api_toggle_switch),
    path("devices/external/setip/<int:id>", views.external_api_set_ip),
    path("devices/external/create_wifi/<int:id>", views.external_api_create_wifi),
    path("devices/external/killnetwork/<int:id>", views.external_api_killnetwork),
    path("devices/external/getinfo/<int:id>", views.external_api_get_info),

    #Graphs
    path('api/graph', views.createGraph),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]