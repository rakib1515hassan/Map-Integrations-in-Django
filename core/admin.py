from django.contrib import admin
from .models import EVChargingLocation, Vehicle


# Register your models here.
admin.site.register(EVChargingLocation)
admin.site.register(Vehicle)

