from django.shortcuts import render

from .models import Battery

def battery_list(request):
    batteries = Battery.objects.all()
    return render(request,'battery/battery_list.html',{'batteries': batteries})


