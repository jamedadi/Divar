from django.urls import path

from account.views import ShowProfileView, EditProfileView

urlpatterns = [
    path('profile/', ShowProfileView.as_view(), name='show-profile'),
    path('edit', EditProfileView.as_view(), name='edit-profile')
]