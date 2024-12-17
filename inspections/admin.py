# inspections/admin.py

from django.contrib import admin
from .models import User, InspectionObject, InspectionResult, IncidentStatus


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username',)


@admin.register(InspectionObject)
class InspectionObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'last_check_date')
    list_filter = ('last_check_date',)
    search_fields = ('name', 'address')
    ordering = ('-last_check_date',)


@admin.register(InspectionResult)
class InspectionResultAdmin(admin.ModelAdmin):
    list_display = ('object', 'inspector', 'date')
    list_filter = ('date', 'inspector')
    search_fields = ('object__name', 'inspector__username')
    ordering = ('-date',)


@admin.register(IncidentStatus)
class IncidentStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'status')
    search_fields = ('status',)
