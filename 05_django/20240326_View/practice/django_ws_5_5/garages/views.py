from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    garages = Garage.objects.all()
    context = {
        'garages': garages
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')

def edit(request, pk):
    garages = Garage.objects.get(pk=pk)
    context = {
        'garages' : garages,
    }
    return render(request, 'garages/edit.html', context)

def update(request, pk):
    garages = Garage.objects.get(pk=pk)
    garages.location = request.POST.get('location')
    garages.capacity = request.POST.get('capacity')
    garages.is_parking_avaliable = request.POST.get('is_parking_avaliable')
    garages.opening_time = request.POST.get('opening_time')
    garages.closing_time = request.POST.get('closing_time')
    garages.save()

    return redirect('garages:index')