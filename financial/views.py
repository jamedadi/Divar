from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from financial.models import Payment, Gateway


class PaymentView(LoginRequiredMixin, View):

    def get(self, request, invoice_number, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404
        gateways = Gateway.objects.filter(is_enable=True)
        return render(request, 'financial/payment_detail.html', context={'payment': payment, 'gateways': gateways})


class PaymentGatewayView(LoginRequiredMixin, View):

    def get(self, request, invoice_number, gateway_code, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404

        try:
            gateway = Gateway.objects.get(gateway_code=gateway_code)
        except Payment.DoesNotExist:
            raise Http404

        payment.gateway = gateway
        payment.save()
        data = payment.get_data()
        request_handler = gateway.get_request_handler()
        result, authority = request_handler(**data)
        payment.authority = authority
        payment.save()
        return redirect(result)


class PaymentVerifyView(LoginRequiredMixin, View):
    template_name = 'financial/callback.html'

    def get(self, request, *args, **kwargs):
        authority = request.GET.get('Authority')
        try:
            payment = Payment.objects.get(authority=authority)
        except Payment.DoesNotExist:
            raise Http404

        request_handler = payment.gateway.get_verify_handler()

        payment.is_paid, ref_id = request_handler(merchant_id=payment.gateway.auth_data, amount=payment.amount,
                                                  authority=payment.authority)
        payment.save()
        return render(request, self.template_name, context={'is_paid': payment.is_paid, 'ref_id': ref_id})
