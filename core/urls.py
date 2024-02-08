from django.urls import path
from core.View import charging_location, vehicle
from core.View import addLocation

urlpatterns = [
    path('', charging_location.index, name='index'),
    path('index2/', charging_location.index2, name='index2'),
    path('get-nearest-station/', charging_location.NearestStation, name='NearestStation'),

    path('index3/', vehicle.vehicle_index, name='index3'),
    path('school-create/', addLocation.SchoolCreateView.as_view(), name='school_create'),

]
