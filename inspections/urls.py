from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home'),
    path('add-object/', views.add_object, name='add_object'),
    path('add-result/', views.add_result, name='add_result'),
]
