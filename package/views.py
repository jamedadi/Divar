from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import View

from advertisement.models import Advertisement
from financial.models import Payment
from package.models import Package
from purchase.models import Purchase


class PackageView(LoginRequiredMixin, View):
    template_name = 'package/package_advertisement.html'

    def get(self, request, package_pk, advertisement_pk):
        package = Package.objects.get(pk=package_pk)
        advertisement = Advertisement.objects.get(pk=advertisement_pk)
        return render(request, self.template_name, {'package': package, 'advertisement': advertisement})

