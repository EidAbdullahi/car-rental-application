from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('rent/', views.rent_car, name='rent_car'),
    path('return/', views.return_car, name='return_car'),
    path('login/', views.login_view, name='login'),  # Update here
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
