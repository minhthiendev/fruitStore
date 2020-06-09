from django.db import models

# Create your models here.
from customers.models import Customer
from Fruits.models import Fruit


class Cart(models.Model):
    fruit = models.ForeignKey(
        Fruit, on_delete=models.CASCADE, related_name='fruits_cart')
    kg = models.IntegerField(default=1)

    own = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customers_cart')

    def __str__(self):
        return self.fruit.title
