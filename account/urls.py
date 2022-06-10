from django.urls import path

from account.views import ProfileView, EditProfileView, RegisterUserView, LoginUserView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='show-profile'),
    path('edit', EditProfileView.as_view(), name='edit-profile'),
    path('register', RegisterUserView.as_view(), name='register-account'),
    path('login', LoginUserView.as_view(), name='login-account')
]