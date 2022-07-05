from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import FormView, DetailView

from advertisement.forms import PostAdvertisementForm
from advertisement.models import Advertisement
from category.models import Category
from package.models import Package
from .filters import AdvertisementFilter


class PostAdvertisementView(FormView):
    """ Get form from PostAdvertisementForm 📢"""

    template_name = 'advertisement/post_advertisement.html'
    form_class = PostAdvertisementForm
    success_url = '/'

    def form_valid(self, form):
        # get user from request
        user = self.request.user
        form.cleaned_data['images'] = self.request.FILES.getlist('files')
        form.save(user)
        return super().form_valid(form)


class AdvertisementDetailView(DetailView):
    """ Get advertisement detail from Advertisement model """

    model = Advertisement
    template_name = 'advertisement/advertisement_detail.html'

    def get(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        packages = Package.objects.filter(is_enable=True)
        return render(request, self.template_name, context={'advertisement': advertisement, 'packages': packages})


class AdvertisementCityListView(View):
    """ Handle list of advertisements by specific city 🏙 """

    def get(self, request, *args, **kwargs):
        city = self.kwargs.get('city')
        queryset = Advertisement.objects.filter(location__city__slug=city)
        filter = AdvertisementFilter(self.request.GET, queryset=queryset)
        categories = Category.objects.all()
        response = render(
            request, 'advertisement/advertisement_list.html',
            context={'filter': filter, 'categories': categories, 'city': city}
        )
        if 'city' not in request.COOKIES:
            response.set_cookie('city', city)
        return response


class AdvertisementCityCategoryListView(View):
    """
    Get advertisement by cities 🏙 and categories 🔠 from Advertisement model
    """

    def get(self, request, *args, **kwargs):
        city = self.kwargs.get('city')
        category = self.kwargs.get('category')
        queryset = Advertisement.objects.filter(location__city__slug=city, category__slug=category)
        categories = Category.objects.all()
        filter = AdvertisementFilter(self.request.GET, queryset=queryset)
        return render(
            request, 'advertisement/advertisement_list.html',
            context={'filter': filter, 'categories': categories, 'city': city}
        )

    def post(self, request, *args, **kwargs):
        form = self.request.AdvertisementFilter(self.request.GET)
        if form.is_valid():
            return render(request, 'advertisement/advertisement_list.html', context={'filter': form.qs})


# A decorator that caches 🔂 the page for 3 minutes.
@method_decorator(cache_page(60 * 3), name='dispatch')
class AdvertisementTehranListView(AdvertisementCityListView):
    """
    This view inherited from AdvertisementCityListView to cache 🔂 Advertisements in "Tehran" City.
    "Tehran" is capital of IRAN 🇮🇷 and it has so many request per seconds ⏳ . This is why we have to cache 🔂 this View
    """

    def get(self, request, *args, **kwargs):
        self.kwargs['city'] = 'tehran'
        return super().get(request, *args, **kwargs)
