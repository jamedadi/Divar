from django.urls import path

from advertisement.views import (
    PostAdvertisementView,
    AdvertisementDetailView,
    AdvertisementCityListView,
    AdvertisementCityCategoryListView,
)

urlpatterns = [
    path(
        "s/<slug:city>/", AdvertisementCityListView.as_view(), name="advertisement-list"
    ),
    path(
        "s/<slug:city>/<slug:category>/",
        AdvertisementCityCategoryListView.as_view(),
        name="advertisement-list-city-category",
    ),
    path("<pk>/", AdvertisementDetailView.as_view(), name="advertisement-detail"),
    path(
        "postadvertisement/", PostAdvertisementView.as_view(), name="post-advertisement"
    ),
]
