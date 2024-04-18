from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups',
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        app_label = 'repair_service'

    def __str__(self):
        return self.username


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Device(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model}"


class RepairTech(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    issue_description = models.TextField()
    repair_status = models.CharField(
        max_length=50,
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='pending'
    )
    repair_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} - {self.repair_status}"


class SparePart(models.Model):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
