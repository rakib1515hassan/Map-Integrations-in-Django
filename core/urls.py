from django.urls import path
from core.View import charging_location, vehicle

urlpatterns = [
    path('', charging_location.index, name='index'),
    path('get-nearest-station/', charging_location.NearestStation, name='NearestStation'),

    path('vehicle/', vehicle.vehicle_index, name='vehicle_index'),

]
