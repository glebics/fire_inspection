# inspections/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('inspector', 'Inspector'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )


class InspectionObject(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    last_check_date = models.DateField()

    def __str__(self):
        return self.name


class InspectionResult(models.Model):
    object = models.ForeignKey(
        InspectionObject, on_delete=models.CASCADE, related_name='results')
    inspector = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'inspector'})
    date = models.DateField()
    findings = models.TextField()
    recommendations = models.TextField()

    def __str__(self):
        return f"{self.object.name} - {self.inspector.username} - {self.date}"


class IncidentStatus(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status
