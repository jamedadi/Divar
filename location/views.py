from django.shortcuts import render, redirect
from django.views import View

from location.models import City


class CitiesListView(View):

    def get(self, request, *args, **kwargs):
        """
        If the user has a cookie, redirect them to the advertisement list page, otherwise render the cities list page
        """
        city = request.COOKIES.get('city')
        if city:
            return redirect('advertisement-list', city=city)
        else:
            cities = City.objects.all()
            return render(request, 'location/cities_list.html', context={'cities': cities})
