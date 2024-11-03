from django.urls import path

from . import views
 
urlpatterns = [
  
     path('', views.battery_list, name='battery_list')
 ]
 