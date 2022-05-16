from django.urls import path

from account.views import ShowProfileView, EditProfileView, RegisterUserView, LoginUserView

urlpatterns = [
    path('profile/', ShowProfileView.as_view(), name='show-profile'),
    path('edit', EditProfileView.as_view(), name='edit-profile'),
    path('register', RegisterUserView.as_view(), name='register-account'),
    path('login', LoginUserView.as_view(), name='login-account')
]