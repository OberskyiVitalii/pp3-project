from django.shortcuts import render, redirect
from .models import Service, Device, RepairTech, SparePart

def index(request):
    services = Service.objects.all()
    return render(request, 'repair_service/index.html', {'services': services})
