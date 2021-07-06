from django.db import models
from PIL import Image

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=False)
    picture = models.ImageField(upload_to="fooditems", blank=False)
    # picture = models.ImageField(default="default.jpg", upload_to="fooditems", blank=False)

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        picture = Image.open(self.picture.path)
        picture.thumbnail((400,400))
        picture.save(self.picture.path)

