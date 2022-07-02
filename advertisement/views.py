from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from advertisement.forms import PostAdvertisementForm
from advertisement.models import Advertisement
from package.models import Package
from .filters import AdvertisementFilter


class PostAdvertisementView(FormView):
    template_name = 'advertisement/post_advertisement.html'
    form_class = PostAdvertisementForm
    success_url = '/'

    def form_valid(self, form):
        # get user from request
        user = self.request.user
        form.cleaned_data['images'] = self.request.FILES.getlist('files')
        form.save(user)
        return super().form_valid(form)


class AdvertisementDetailView(View):
    template_name = 'advertisement/advertisement_detail.html'

    def get(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        packages = Package.objects.filter(is_enable=True)
        return render(request, self.template_name, context={'advertisement': advertisement, 'packages': packages})


class AdvertisementCityListView(View):

    def get(self, request, *args, **kwargs):
        city = self.kwargs.get('city')

        queryset = Advertisement.objects.filter(location__city__slug=city)
        filter = AdvertisementFilter(self.request.GET, queryset=queryset)
        response = render(request, 'advertisement/advertisement_list.html', context={'filter': filter})
        if 'city' not in request.COOKIES:
            response.set_cookie('city', city)
        return response

    def post(self, request, *args, **kwargs):
        form = self.request.AdvertisementFilter(self.request.GET)
        if form.is_valid():
            return render(request, 'advertisement/advertisement_list.html', context={'filter': form.qs})


class AdvertisementCityCategoryListView(View):

    def get(self, request, *args, **kwargs):
        city = self.kwargs.get('city')
        category = self.kwargs.get('category')
        queryset = Advertisement.objects.filter(location__city__slug=city, category__slug=category)
        filter = AdvertisementFilter(self.request.GET, queryset=queryset)
        return render(request, 'advertisement/advertisement_list.html', context={'filter': filter})

    def post(self, request, *args, **kwargs):
        form = self.request.AdvertisementFilter(self.request.GET)
        if form.is_valid():
            return render(request, 'advertisement/advertisement_list.html', context={'filter': form.qs})

