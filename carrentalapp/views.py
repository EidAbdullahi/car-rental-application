from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarRental, CarReturn
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import CarRentalForm, CarReturnForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Django is working!")


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'carrentalapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'carrentalapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request):
    return render(request, 'profile.html') 

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Services Page
def services(request):
    return render(request, 'services.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Car Rental Form (Booking a Car)


@login_required
def rent_car(request):
    if request.method == 'POST':
        form = CarRentalForm(request.POST, request.FILES)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.save()
            return redirect('home')
    else:
        form = CarRentalForm()
    return render(request, 'rent_car.html', {'form': form})

@login_required
def return_car(request):
    if request.method == 'POST':
        form = CarReturnForm(request.POST, request.FILES)
        if form.is_valid():
            rental_id = request.POST['rental_id']
            rental = CarRental.objects.get(id=rental_id, user=request.user)
            car_return = form.save(commit=False)
            car_return.rental = rental
            car_return.save()
            return redirect('home')
    else:
        form = CarReturnForm()
    rentals = CarRental.objects.filter(user=request.user)
    return render(request, 'return_car.html', {'form': form, 'rentals': rentals})
    

