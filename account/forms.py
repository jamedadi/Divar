from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.db.models import Q

User = get_user_model()


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


class RegisterAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class LoginAccountForm(forms.Form):
    username_or_phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(
            Q(phone_number=self.cleaned_data['username_or_phone']) | Q(email=self.cleaned_data['username_or_phone'])
        ).first()
        if user is None:
            raise forms.ValidationError('email or phone number you entered is not correct')

        if not user.password == self.cleaned_data['password']:
            raise forms.ValidationError('password is wrong')

        self.cleaned_data['user'] = user
        return self.cleaned_data



