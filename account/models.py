from django.db import models
from django.contrib.auth.models import User
from advertisement.models import Advertisement


class Profile(models.Model):
    """"
    This model represent a profile of a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)  
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name="advertisements")
    modified_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now=True)