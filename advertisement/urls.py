from django.urls import path

from advertisement.views import PostAdvertisementView, AdvertisementDetailView, AdvertisementListView

urlpatterns = [
    path('postadvertisement', PostAdvertisementView.as_view(), name='post-advertisement'),
    path('<pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),
    path('<str:city>', AdvertisementListView.as_view(), name='advertisement-list')
]