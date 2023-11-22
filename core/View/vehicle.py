from django.shortcuts import render
from core.models import Vehicle
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse

import folium
from folium.plugins import FastMarkerCluster
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Create your views here.
def vehicle_index(request):


    context = {
        # '': ,
    }
    
    return render(request, 'index_3.html', context)