from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarRental, CarReturn
from django.contrib.auth.models import User
from .models import UserProfile

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
        car_model = request.POST['car_model']
        duration = request.POST['duration']
        picture = request.FILES['picture']
        amount_paid = request.POST['amount_paid']
        fuel_used = request.POST['fuel_used']

        rental = CarRental.objects.create(
            user=request.user,
            car_model=car_model,
            duration=duration,
            picture=picture,
            amount_paid=amount_paid,
            fuel_used=fuel_used
        )
        rental.save()
        return redirect('home')

    return render(request, 'rent_car.html')

# Car Return Form (Returning a Car)
@login_required
def return_car(request):
    if request.method == 'POST':
        rental_id = request.POST['rental_id']
        car_picture = request.FILES['car_picture']
        condition = request.POST['condition']
        issues = request.POST.get('issues', '')

        rental = CarRental.objects.get(id=rental_id, user=request.user)
        car_return = CarReturn.objects.create(
            rental=rental,
            car_picture=car_picture,
            condition=condition,
            issues=issues
        )
        car_return.save()
        return redirect('home')

    rentals = CarRental.objects.filter(user=request.user)
    return render(request, 'return_car.html', {'rentals': rentals})

