from django.urls import path

from purchase.views import PurchaseCreateView

urlpatterns = [
    path('<int:package_pk>/<int:advertisement_pk>/', PurchaseCreateView.as_view(), name='purchase-create'),
]