from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-nearest-station/', views.NearestStation, name='NearestStation'),
]
