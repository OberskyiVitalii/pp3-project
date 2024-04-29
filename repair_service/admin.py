from django.contrib import admin

from .models import Service, Device, ServiceCenter, RepairOrder

admin.site.register(Service)
admin.site.register(ServiceCenter)
admin.site.register(Device)
admin.site.register(RepairOrder)
