from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import View

from advertisement.models import Advertisement
from financial.models import Payment
from package.models import Package
from purchase.models import Purchase


class PurchaseCreateView(LoginRequiredMixin,View):
    template_name = 'purchase/create.html'

    def get(self, request, package_pk, advertisement_pk):
        if not Advertisement.is_belong_user(request.user, advertisement_pk):
            raise Http404

        try:
            package = Package.objects.get(pk=package_pk)
        except Package.DoesNotExist:
            raise Http404

        try:
            advertisement = Advertisement.objects.get(pk=advertisement_pk)
        except Advertisement.DoesNotExist:
            raise Http404

        purchase = Purchase.create(package=package, user=request.user, advertisement=advertisement)
        return render(request, self.template_name , {'purchase': purchase})


