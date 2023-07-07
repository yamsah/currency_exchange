from django.db import models
import datetime

# Create your models here.

class Transaction(models.Model):
    currency_one = models.CharField(max_length=10)
    amount_one = models.DecimalField(max_digits=13,decimal_places=2)
    currency_two = models.CharField(max_length=10)
    amount_two = models.DecimalField(max_digits=13,decimal_places=2)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
         f"{self.currency_one} {self.amount_one} to {self.currency_two} {self.amount_two}"


