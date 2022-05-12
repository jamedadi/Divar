import django_filters

from advertisement.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')

    class Meta:
        model = Advertisement
        fields = ['title']