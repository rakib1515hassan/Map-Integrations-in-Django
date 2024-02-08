from django.shortcuts import render
from core.models import EVChargingLocation
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse

import folium
from folium.plugins import FastMarkerCluster
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Create your views here.
def index(request):

    ## NOTE:- For index_1.html------------------------------------------------------
    stations = EVChargingLocation.objects.all()


    # If we only generate clusters for graterthen the average values, then
    # avg_lat  = EVChargingLocation.objects.aggregate(avg = Avg('latitude'))['avg']
    # stations = EVChargingLocation.objects.exclude(latitude__gt = avg_lat)
    
    
    m = folium.Map(
            location   = [41.5025, -72.699997], 
            zoom_start = 9,
            # position="absolute",
            # left="0%",
            # width="100%",
            # height="100%",
        )
    # This show all pints but FastMarkerCluster show the cluster of the points.
    # for station in stations:
    #     coordinates = ( station.latitude, station.longitude )
    #     folium.Marker( coordinates, popup= station.station_name).add_to(m)

    # Use FastMarkerCluster to generate a the cluster on the map.
    # That's why, we pass the list of all (latitude,longitude) tuples in the data.
    latitudes  = [station.latitude  for station in stations]
    longitudes = [station.longitude for station in stations]
    FastMarkerCluster(data = list(zip(latitudes, longitudes))).add_to(m)


    context = {
        'map': m._repr_html_(),
        'stations': stations,
    }
    
    return render(request, 'index_1.html', {'map': m._repr_html_()})








## NOTE:- For index_2.html--------------------------------------------------------
def index2(request):
    stations = list(EVChargingLocation.objects.values('latitude', 'longitude')[:10])

    # print("-----------------")
    # print("Result = ", stations)
    # print("-----------------")
    
    return render(request, 'index_2.html', {'stations': stations})







def NearestStation(request):
    lat  = request.GET.get('latitude')
    lng= request.GET.get('longitude')
    # print("-----------------")
    # print("lat = ", lat)
    # print("lng = ", lng)
    # print("-----------------")
    user_location = lat, lng

    station_distance = {}
    for station in EVChargingLocation.objects.all()[:10]:
        station_location = station.latitude, station.longitude

        # Now Calculate distance between the user location and the station
        distance = geodesic(user_location, station_location).km   # miles, km, etc.
        station_distance[distance] = station_location
    
    min_station = min(station_distance)
    station_coords = station_distance[min_station] 
    # print("-----------------")
    # # print("distance = ", min_station)
    # print("station_coords = ", station_coords)
    # print("-----------------")
    data = {
        "coordinates": station_coords,
        "distance"   : min_station,        
    }

    return JsonResponse(data)