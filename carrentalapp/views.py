from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarRental, CarReturn
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import CarRentalForm, CarReturnForm


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
    

