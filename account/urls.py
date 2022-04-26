from django.urls import path

from account.views import ShowProfileView, EditProfileView, RegisterView

urlpatterns = [
    path('profile/', ShowProfileView.as_view(), name='show-profile'),
    path('edit', EditProfileView.as_view(), name='edit-profile'),
    path('register', RegisterView.as_view(), name='register-account')
]