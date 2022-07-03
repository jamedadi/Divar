from django.shortcuts import render
from django.views import View

from category.models import Category


class CategoryListView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        city = request.COOKIES.get('city')
        return render(request, 'category.', context={'categories': categories, 'city': city})