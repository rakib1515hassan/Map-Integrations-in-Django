from django.contrib import admin
from .models import EVChargingLocation, Vehicle, School


# Register your models here.
admin.site.register(EVChargingLocation)
admin.site.register(Vehicle)
admin.site.register(School)

