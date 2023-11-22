from django.urls import path
from core.View import charging_location

urlpatterns = [
    path('', charging_location.index, name='index'),
    path('get-nearest-station/', charging_location.NearestStation, name='NearestStation'),
]
