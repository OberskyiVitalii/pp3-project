from django.db import models
from django.contrib.auth import get_user_model


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Device(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=0)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cpu = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.brand} {self.model}"


class ServiceCenter(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, unique=True)
    work_time = models.CharField(max_length=30)

    def __str__(self):
        return self.address
    

class RepairOrder(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'Pending'
        IN_PROGRESS = 'In Progress'
        COMPLETED = 'Completed'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    service_center = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    status = models.CharField(max_length=50, choices=StatusChoice.choices, default=StatusChoice.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order for {self.device} at {self.service_center}. Status: {self.status}"