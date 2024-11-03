from django.db import models
from vehicle_data.models import Vehicle

class Telemetry(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="telemetry")
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    efficiency = models.DecimalField( max_digits=5, decimal_places=2)

