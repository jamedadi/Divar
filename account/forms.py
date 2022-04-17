from django.forms import ModelForm

from account.models import Profile


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']
