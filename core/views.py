from django.shortcuts import render
from .models import EVChargingLocation
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    stations = list(EVChargingLocation.objects.values('latitude', 'longitude')[:10])
    # print("-----------------")
    # print("Result = ", stations)
    # print("-----------------")
    context = {
        'stations': stations,
    }
    return render(request, 'index.html', context)


def NearestStation(request):
    lat  = request.GET.get('latitude')
    lng= request.GET.get('longitude')
    print("-----------------")
    print("lat = ", lat)
    print("lng = ", lng)
    print("-----------------")

    data = {

    }

    return JsonResponse(data)