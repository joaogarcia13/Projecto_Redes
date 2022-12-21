from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

# URL Configs
urlpatterns = [
    path('devices/list/', views.device_listing),
    # path('devices/<int:device_id>/', views.device_detail, name='device-detail'),
    # path('devices/search/', views.device_search, name='device-search'),

    # The home page
    path('devices/', views.index, name='home'),
    # path('login', views.login, name='login'),
    # path('pages', views.pages, name='pages'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    path('api/devices', views.getDevice, name=''),

    # API
    # re_path('r"^devices$"', views.deviceAPI),
    # re_path('r"^devices/([0-9]+)$"', views.deviceAPI),
    # url(r'^device$',views.deviceAPI),
    # url(r'^device/([0-9]+)$',views.deviceAPI),
]