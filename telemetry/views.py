from django.shortcuts import render

from .models import Telemetry

def telemetry_list(request):
    telemetry_data = Telemetry.objects.all()
    return render(request, 'telemetry/telemetry_list.html',{'telemetry_data': telemetry_data})
