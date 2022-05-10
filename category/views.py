from django.views.generic import ListView

from category.models import Category


class ListAllCategoriesView(ListView):
    model = Category
    template_name = 'category/all_categories.html'