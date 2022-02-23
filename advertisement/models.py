from django.db import models

from account.models import Profile
from category.models import Category
from location.models import Location


class Advertisement(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='advertisements')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="advertisements")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='advertisements')
    
    def __str__(self):
        return f"{self.title} > {self.location.city.name}"
    
    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = "Advertisements"