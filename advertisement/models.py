from django.db import models
from category.models import Category
from location.models import Location


class Advertisement(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} > {self.location.name}"
