from django import forms

from advertisement.models import Advertisement, AdvertisementImage
from category.models import Category
from location.models import Location


class PostAdvertisementForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    images = forms.ImageField()

    def clean(self):
        return self.cleaned_data