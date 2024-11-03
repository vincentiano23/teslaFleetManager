from django.db import models

class Vehicle(models.Model):
    model_name = models.CharField( max_length=50)
    year = models.IntegerField()
    battery_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    max_range = models.CharField(max_length=100)


