from django.db import models
from vehicle_data.models import Vehicle
 
class Battery(models.Model):
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="batteries")
    charge_cycles = models.IntegerField()
    health_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
