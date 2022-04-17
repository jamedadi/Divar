from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """"
    This model represent a profile of a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=50, verbose_name='last name')
    phone_number = models.CharField(max_length=20, verbose_name='phone number', unique=True)
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name='updated time of profile')
    created_time = models.DateTimeField(auto_now=True, verbose_name='created time of profile')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'