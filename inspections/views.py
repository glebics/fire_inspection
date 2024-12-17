# inspections/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, InspectionObjectForm, InspectionResultForm
from .models import InspectionObject, InspectionResult

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'inspections/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'inspections/register.html', {'form': form})


@login_required
def home(request):
    objects = InspectionObject.objects.all()
    if request.user.role == 'admin':
        results = InspectionResult.objects.all()
    else:
        results = InspectionResult.objects.filter(inspector=request.user)

    context = {
        'objects': objects,
        'results': results,
    }
    return render(request, 'inspections/home.html', context)


@login_required
def add_object(request):
    if request.method == 'POST':
        form = InspectionObjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InspectionObjectForm()
    return render(request, 'inspections/add_object.html', {'form': form})


@login_required
def add_result(request):
    if request.method == 'POST':
        form = InspectionResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InspectionResultForm()
    return render(request, 'inspections/add_result.html', {'form': form})
