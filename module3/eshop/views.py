from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from .models import Product, User
from .forms import RegistrationForm
from django.urls import reverse_lazy

class MainPageView(ListView):
    model = Product
    template_name = "main.html"
    context_object_name = "products"

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("main")
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
