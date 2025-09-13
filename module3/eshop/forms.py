from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

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
    def clean_password2(self):
        password2 = self.cleaned_data.get("password1")
        return password2