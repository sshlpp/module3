from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Product, User
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class MainPageView(ListView):
    model = Product
    template_name = "main.html"
    context_object_name = "products"

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("main")
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")  
    #     return super().form_valid(form)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect(self.get_success_url())
