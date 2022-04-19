from django.forms import ModelForm

from account.models import User


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']