from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"