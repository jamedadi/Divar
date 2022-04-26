from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


class RegisterAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
    # username = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    #
    # def clean(self):
    #     """
    #     Clean the form data and check if email exists.
    #     """
    #     if User.objects.filter(email=self.cleaned_data['email']).exists():
    #         raise forms.ValidationError('Email already registered')
    #
    #     return self.cleaned_data
    #
    # def save(self):
    #     """
    #     Create a new user and save it to the database.
    #     """
    #     user = User.objects.create_user(**self.cleaned_data)
    #     return user
