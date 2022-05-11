from django.urls import path

from advertisement.views import PostAdvertisementView, AdvertisementDetailView, AdvertisementListView, \
    AdvertisementCityCategoryListView

urlpatterns = [
    path('postadvertisement', PostAdvertisementView.as_view(), name='post-advertisement'),
    path('<pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),
    path('<slug:city>', AdvertisementListView.as_view(), name='advertisement-list'),
    path('<slug:city>/<slug:category>', AdvertisementCityCategoryListView.as_view(),
         name='advertisement-list-city-category')
]