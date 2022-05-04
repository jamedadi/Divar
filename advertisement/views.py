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
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)

