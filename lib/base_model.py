from django.db import models


class BaseModel(models.Model):
    """
    A base model that other models inherit from it
    To add created_time and modified_time fields to them.
    """

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
