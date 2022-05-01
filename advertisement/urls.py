from django.urls import path

from advertisement.views import PostAdvertisementView

urlpatterns = [
    path('postadvertisement', PostAdvertisementView.as_view(), name='post-advertisement')
]