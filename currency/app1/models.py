from django.db import models

# Create your models here.

class Transaction(models.Model):
    currency1 = models.CharField(max_length=10)
    currency2 = models.CharField(max_length=10)
    price1 = models.IntegerField(default=0)
    price2 = models.IntegerField(default=0)
