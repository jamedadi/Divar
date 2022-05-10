from django.db import models

from lib.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
