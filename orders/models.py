from django.db import models
from customers.models import Customer
from Fruits.models import Fruit
from datetime import datetime
# Create your models here.


class Order(models.Model):
    own = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customers_order')
    fruit = models.ForeignKey(
        Fruit, on_delete=models.CASCADE, related_name='fruits_order')
    kg = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=255, default='spending')

    def __str__(self):
        return self.own.name
