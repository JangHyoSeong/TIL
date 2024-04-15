from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import LocationListSerializer, StationSerializer, StationListSerializer, StationDetailSerializer
from .models import Location, Station, Car


# Create your views here.
@api_view(['GET', 'POST'])
def location_list(request):
    if request.method == 'GET':
        locations = get_list_or_404(Location)
        serializer = LocationListSerializer(locations, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = LocationListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_station(request, location_pk):
    if request.method == 'POST':
        location = get_object_or_404(Location, pk=location_pk)
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def station_list(request):
    if request.method == 'GET':
        stations = get_list_or_404(Station)
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def station_detail(request, station_pk):
    if request.method == 'GET':
        station = get_object_or_404(Station, pk=station_pk)
        serializer = StationDetailSerializer(station)
        return Response(serializer.data)