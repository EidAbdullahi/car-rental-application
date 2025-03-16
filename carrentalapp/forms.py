from django import forms
from .models import CarRental, CarReturn

class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ['car_model', 'duration', 'picture', 'amount_paid', 'fuel_used']
        widgets = {
            'car_model': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'fuel_used': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CarReturnForm(forms.ModelForm):
    class Meta:
        model = CarReturn  # Ensure this model exists
        fields = ['return_date', 'car_picture', 'condition', 'issues']
        widgets = {
            'return_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'car_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'condition': forms.Textarea(attrs={'class': 'form-control'}),
            'issues': forms.Textarea(attrs={'class': 'form-control'}),
        }