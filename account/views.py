from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, UpdateView


from account.forms import EditProfileForm, RegisterAccountForm, LoginAccountForm
from account.models import User
from lib.username import generate_random_string


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    """
    Show user profile and all advertisements posted by user
    """
    model = User
    template_name = 'account/profile.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['user'] = self.request.user
        return context


class EditProfileView(UpdateView):
    """
    Edit user profile
    """
    model = User
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('show-profile')
    slug_field = "phone_number"

    def get_object(self, queryset=None):
        return self.request.user


class RegisterUserView(FormView):
    """
    Register new user by email or phone number
    """
    template_name = 'account/register.html'
    form_class = RegisterAccountForm
    success_url = '/'

    def form_valid(self, form):
        """
        To get user instance and assign a random username to username field of user
        """
        instance = form.save(commit=False)
        instance.username = generate_random_string()
        instance.save()
        return super().form_valid(form)


class LoginUserView(FormView):
    """
    Login View to sign-in user by Email or Phone number
    """
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


