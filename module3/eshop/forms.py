from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Purchase, User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "reg-form",
                "placeholder": "Enter username"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Enter password"
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Confirm your password"
            }),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={ 
                'class': 'purchase-input',
                'min': 1,
                'placeholder': 'Введите количество'
            })
        }
