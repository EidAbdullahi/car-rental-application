from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('rent/', views.rent_car, name='rent_car'),
    path('return/', views.return_car, name='return_car'),
    
]
