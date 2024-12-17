# inspections/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, InspectionObject, InspectionResult


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class InspectionObjectForm(forms.ModelForm):
    class Meta:
        model = InspectionObject
        fields = ['name', 'address', 'description', 'last_check_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'last_check_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class InspectionResultForm(forms.ModelForm):
    class Meta:
        model = InspectionResult
        fields = ['object', 'inspector', 'date', 'findings', 'recommendations']
        widgets = {
            'object': forms.Select(attrs={'class': 'form-select'}),
            'inspector': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'findings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'recommendations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
