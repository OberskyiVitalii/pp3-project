from django.contrib import admin

from .models import Service, Device, ServiceCenter, SparePart, RepairOrder

admin.site.register(Service)
admin.site.register(ServiceCenter)
admin.site.register(Device)
admin.site.register(SparePart)
admin.site.register(RepairOrder)
