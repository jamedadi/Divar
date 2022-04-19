from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, UpdateView

from account.forms import EditProfileForm
from account.models import User


@method_decorator(login_required, name='dispatch')
class ShowProfileView(TemplateView):
    model = User
    template_name = 'account/profile.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        user = self.request.user
        context['profile'] = User.objects.filter(user=user).first()
        return context


class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('show-profile')
    slug_field = "phone_number"

    def get_object(self, queryset=None):
        return self.request.user.profile


    # def form_valid(self, form):
        # instance = form.save(commit=False)
        # instance.user = self.request.user
        # instance.save()
        # return super().form_valid(form)