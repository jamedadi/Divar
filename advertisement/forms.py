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
    # images = forms.FileField()

    # def image_clean(self):
    #     self.cleaned_data['images'].__dict__['name'] = self.cleaned_data.['images']

    def save(self, user):
        self.cleaned_data['user'] = user
        Advertisement.add(
            user=user,
            title=self.cleaned_data.get('title'),
            description=self.cleaned_data.get('description'),
            price=self.cleaned_data.get('price'),
            location=self.cleaned_data.get('location'),
            category=self.cleaned_data.get('category'),
            images=self.cleaned_data.get('images')
        )