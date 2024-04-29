from django import forms
from .models import Device, Service, ServiceCenter, RepairOrder
from django.contrib.auth.models import User


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

    
class ServiceCenterForm(forms.ModelForm):
    class Meta:
        model = ServiceCenter
        fields = ['address', 'phone_number', 'work_time']


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['brand', 'model', 'cpu', 'gpu', 'ram']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class StatusForm(forms.ModelForm):
    class Meta:
        model = RepairOrder
        fields = ['status']