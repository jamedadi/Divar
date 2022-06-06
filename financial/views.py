from django.shortcuts import render
from django.views import View


class GatewayView(View):
    template_name = 'finance/payment.html'

    def get(self, request, *args, **kwargs):
        


        return render(request, self.template_name, )