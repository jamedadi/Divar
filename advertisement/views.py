from django.views.generic import FormView

from advertisement.forms import PostAdvertisementForm

class PostAdvertisementView(FormView):
    template_name = 'advertisement/post_advertisement.html'
    form_class = PostAdvertisementForm
    success_url = '/'


    def form_valid(self, form):
        """
        Get User from request
        """
        user = self.request.user
        form.cleaned_data['images'] = self.request.FILES.getlist('files')
        # form.cleaned_data['user'] = user
        form.save(user)
        return super().form_valid(form)

