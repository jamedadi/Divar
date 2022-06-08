from django.urls import path

from financial.views import PaymentGatewayView, PaymentView, PaymentVerifyView

urlpatterns = [
    path('verify/', PaymentVerifyView.as_view()),
    path('pay/<str:invoice_number>/', PaymentView.as_view(), name='payment-link'),
    path('pay/<str:invoice_number>/<str:gateway_code>/', PaymentGatewayView.as_view(), name='payment-gateway')
]