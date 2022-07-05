from django.urls import path, re_path

from advertisement.views import PostAdvertisementView, AdvertisementDetailView, AdvertisementCityListView, \
    AdvertisementCityCategoryListView, AdvertisementTehranListView

urlpatterns = [
    # Cached URL 🔂
    re_path(r'\btehran\b/', AdvertisementTehranListView.as_view()),

    path('<slug:city>/', AdvertisementCityListView.as_view(), name='advertisement-list'),
    path('<slug:city>/<slug:category>/', AdvertisementCityCategoryListView.as_view(),
         name='advertisement-list-city-category'),
    path('<pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),
    path('postadvertisement/', PostAdvertisementView.as_view(), name='post-advertisement'),
]
