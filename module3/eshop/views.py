from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Product, User
from .forms import PurchaseForm, RegistrationForm
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

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object, backend="django.contrib.auth.backends.ModelBackend")
        return redirect(self.get_success_url())

class PurchaseView(FormView):
    form_class = PurchaseForm
    template_name = "purchase.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']  # получаем pk из URL
        product = get_object_or_404(Product, pk=pk)
        context['product'] = product  # передаем объект в шаблон
        return context
