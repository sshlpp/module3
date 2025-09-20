from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Product, User, Purchase
from .forms import PurchaseForm, RegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db import transaction


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
    
    def get_success_url(self):
        return reverse_lazy("main")

    def form_valid(self, form):
        product_pk = self.kwargs['pk']
        product = get_object_or_404(Product, pk=product_pk)
        quantity = form.cleaned_data['quantity']

        with transaction.atomic():

            product = Product.objects.select_for_update().get(pk=product_pk)

            if product.stock < quantity:
                form.add_error("quantity", "На складе недостаточно товара")
                return self.form_invalid(form)

            total_price = product.price * quantity

            if total_price > self.request.user.wallet:
                form.add_error(None, "Недостаточно средств в кошелькеа")
                return self.form_invalid(form)
            
            Purchase.objects.create(
                user = self.request.user,
                product = product,
                quantity = quantity
            )

            product.stock -= quantity
            product.save

            self.request.user.wallet -= total_price
            self.request.user.save()

            messages.success(self.request, "Покупка успошно совершена")

            return super().form_valid(form)
            
        

        


        


