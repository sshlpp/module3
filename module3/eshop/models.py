from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Return(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
