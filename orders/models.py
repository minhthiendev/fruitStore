from django.db import models
from customers.models import Customer
from Fruits.models import Fruit
from datetime import datetime
# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    total_price = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=255, default='spending')

    def __str__(self):
        return self.name


class fruitOfOrder(models.Model):
    fruit = models.ForeignKey(
        Fruit, related_name='fruit_order', on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, related_name='order_fruit', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.fruit
