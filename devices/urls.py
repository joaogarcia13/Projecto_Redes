from django.urls import path, re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

# URL Configs
urlpatterns = [
    path('list/', views.device_listing),
    # path('devices/<int:device_id>/', views.device_detail, name='device-detail'),
    # path('devices/search/', views.device_search, name='device-search'),

    # The home page
    path('', views.index, name='home'),
    # path('login', views.login, name='login'),
    # path('pages', views.pages, name='pages'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    # API
    # path(r'^device$',views.deviceAPI),
    # path(r'^device/([0-9]+)$',views.devices),
]