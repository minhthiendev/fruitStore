from django.db import models
from datetime import datetime

# Create your models here.


class Fruit (models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    available = models.FloatField(default=0)
    expired = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class ImageFruit (models.Model):
    image = models.ImageField(upload_to="images/")
    fruit = models.ForeignKey(
        Fruit, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.image.url

    def get_url(self):
        return self.image.url

    def to_dict_url(self):
        return {"image": self.image.url}
