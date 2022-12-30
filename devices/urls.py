from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

# URL Configs
urlpatterns = [
    path('devices/list/', views.device_listing),
    path('devices/<int:id>', views.device_details),
    # path('devices/<int:device_id>/', views.device_detail, name='device-detail'),
    # path('devices/search/', views.device_search, name='device-search'),

    # The home page
    path('devices/', views.index, name='home'),
    path('login', views.pages, name='login'),
    path('register', views.pages, name='register'),
    path('ui-maps', views.pages),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    # API
    path('api/devices', views.getDevice),
    path('api/devices/new', views.setDevice),
    path('api/devices/<int:id>/update', views.updateDevice),
    path('api/devices/<int:id>/delete', views.deleteDevice),

    # External API
    path("devices/external/switch_on/<int:id>", views.external_api_switch_on),
    path("devices/external/switch_off/<int:id>", views.external_api_switch_off),
    path("devices/external/setip/<int:id>", views.external_api_switch_off),
    path("devices/external/create_wifi/<object>", views.external_api_create_wifi),
    path('devices/new', views.formDevice),
]