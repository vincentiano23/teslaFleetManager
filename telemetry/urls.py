from django.urls import path
from . import views

urlpatterns = [
    path('',views.telemetry_list, name='telemetry_list')
    
]
