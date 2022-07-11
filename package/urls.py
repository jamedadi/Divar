from django.urls import path

from package.views import PackageView

urlpatterns = [
    path('<int:package_pk>/<int:advertisement_pk>/', PackageView.as_view(), name='package-detail'),
]
