from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import View

from advertisement.models import Advertisement
from financial.models import Payment
from package.models import Package
from purchase.models import Purchase


class PurchaseCreateView(LoginRequiredMixin ,View):

    def get(self, request, package_pk, advertisement_pk):
        try:
            package = Package.objects.get(pk=package_pk)
        except Package.DoesNotExist:
            raise Http404

        advertisement = Advertisement.objects.get(pk=advertisement_pk)
        package = Package.objects.get(pk=package_pk)

        purchase = Purchase.create(package=package, user=request.user, advertisement=advertisement)
        return render(request, 'purchase/create.html', {'purchase': purchase})

