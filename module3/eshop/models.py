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
