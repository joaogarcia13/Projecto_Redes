from django.urls import path, re_path
from . import views

# URL Configs
urlpatterns = [
    path('list/', views.device_listing),
    # path('devices/<int:device_id>/', views.device_detail, name='device-detail'),
    # path('devices/search/', views.device_search, name='device-search'),

    # The home page
    path('', views.index, name='home'),
    # path('pages', views.pages, name='pages'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
]