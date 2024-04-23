from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Device, SparePart, ServiceCenter, RepairOrder
from .forms import DeviceForm, ServiceForm, ServiceCenterForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def home_page(request):
    services = Service.objects.all()
    service_centers = ServiceCenter.objects.all()
    context = {'services': services, 'service_centers': service_centers}
    return render(request, 'repair_service/home_page.html', context)


def detail_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    context = {'service': service}
    return render(request, 'repair_service/service_detail.html', context)


@login_required
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair:home_page')
    else:
        form = ServiceForm()
    
    return render(request, 'service/create_service.html', {'form': form})
    

@login_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('repair:home_page')
    
    return render(request, 'service/delete_service.html', {'service': service})


@login_required
def edit_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('repair:detail_service', service_id = service_id)
    else:
        form = ServiceForm(instance=service)

    return render(request, 'service/edit_service.html', {'form': form})


@login_required
def create_service_center(request):
    if request.method == 'POST':
        form = ServiceCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair:home_page')
    else:
        form = ServiceCenterForm

    return render(request, 'service_center/create_service_center.html', {'form': form})


@login_required
def delete_service_center(request, service_center_id):
    service_center = get_object_or_404(ServiceCenter, id=service_center_id)
    if request.method == 'POST':
        service_center.delete()
        return redirect('repair:home_page')
    
    return render(request, 'service_center/delete_service_center.html', {'service_center': service_center})


@login_required
def edit_service_center(request, service_center_id):
    service_center = get_object_or_404(ServiceCenter, id=service_center_id)
    if request.method == 'POST':
        form = ServiceCenterForm(request.POST, instance=service_center)
        if form.is_valid():
            form.save()
            return redirect('repair:home_page')
    else:
        form = ServiceCenterForm(instance=service_center)

    return render(request, 'service_center/edit_service_center.html', {'form': form})


@login_required
def profile(request):
    devices = Device.objects.filter(user=request.user)
    repair_orders = RepairOrder.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'devices': devices,
        'repair_orders': repair_orders,
    }

    return render(request, 'user/profile.html', context)


@login_required
def order_service(request):
    if request.method == 'POST':
        device_id = request.POST.get('device')
        service_center_id = request.POST.get('choice')
        services_ids = request.POST.getlist('repair_service')
        device = Device.objects.get(id=device_id)
        service_center = ServiceCenter.objects.get(id=service_center_id)
        services = Service.objects.filter(id__in=services_ids)
        repair_order = RepairOrder.objects.create(
            user=request.user,
            device=device,
            service_center=service_center,
            status='Pending'
        )
        repair_order.services.set(services)
        return redirect('repair:profile')
    else:
        devices = Device.objects.filter(user=request.user)
        service_centers = ServiceCenter.objects.all()
        services = Service.objects.all()
        context = {
            'devices': devices,
            'service_centers': service_centers,
            'services': services,
        }

        return render(request, 'repair_service/order_service.html', context)


@login_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.user_id = request.user.id
            device.save()
            return redirect('repair:profile')
    else:
        form = DeviceForm()

    return render(request, 'device/add_device.html', {'form': form})


@login_required
def delete_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
        device.delete()
        return redirect('repair:profile')

    return render(request, 'device/delete_device.html', {'device': device})    


@login_required
def edit_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('repair:profile')
    else:
        form = DeviceForm(instance=device)

    return render(request, 'device/edit_device.html', {'form': form})


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('repair:profile')
    else:
        form = UserProfileForm(instance=user)
    
    context = {
        'form': form,
    }
    return render(request, 'repair_service/update_profile.html', context)