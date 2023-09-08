from django.db import models
from django.core.validators import MinValueValidator 
from decimal import Decimal
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    brand = models.CharField(max_length=50, default="N/A")
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    qty = models.PositiveIntegerField(default=0)
    expiry = models.DateField("Expiry (YYYY-MM-DD)", default=datetime.now)

    def __str__(self):
        return self.name