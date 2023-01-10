from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

# URL Configs
urlpatterns = [
    # The home page
    path('', views.index, name='index'),
    path('devices/', views.index, name='home'),
    path('devices/<int:id>', views.device_details),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.pages, name='register'),
    path('devices/new', views.formDevice),

    # API
    path('api/devices', views.getDevice),
    path('api/devices/new', views.setDevice),
    path('api/devices/<int:id>/update', views.updateDevice),
    path('api/devices/<int:id>/delete', views.deleteDevice),

    # External API
    path("devices/external/switch_on/<int:id>", views.external_api_switch_on),
    path("devices/external/switch_off/<int:id>", views.external_api_switch_off),
    path("devices/external/setip/<int:id>", views.external_api_set_ip),
    path("devices/external/create_wifi/<int:id>", views.external_api_create_wifi),
    path("devices/external/getinfo/<int:id>", views.external_api_get_info),

    #Graphs
    path('api/graph', views.createGraph),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]