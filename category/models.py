from django.db import models

from lib.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, null=True, blank=True, allow_unicode=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
