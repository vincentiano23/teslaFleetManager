from django.shortcuts import render

from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request,'vehicle_data/vehicle_list.html', {'vehicles': vehicles})
