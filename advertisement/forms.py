from django import forms

from advertisement.models import Advertisement


class PostAdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'location', 'category']
