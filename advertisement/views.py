from django.views.generic import FormView, DetailView, ListView

from advertisement.forms import PostAdvertisementForm
from advertisement.models import Advertisement


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
        form.save(user)
        return super().form_valid(form)


class AdvertisementDetailView(DetailView):
    model = Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'

    def get_queryset(self):
        city = self.kwargs['city']
        queryset = super().get_queryset()
        return queryset.filter(location__city__name=city)


class AdvertisementCityCategoryListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = self.request.path_info.split('/')[2]
        return context

    def get_queryset(self):
        city = self.kwargs.get('city')
        category = self.kwargs.get('category')
        queryset = super().get_queryset()
        return queryset.filter(location__city__slug=city, category__slug=category)
