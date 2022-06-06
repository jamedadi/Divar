from django.shortcuts import render
from django.views import View

from advertisement.models import Advertisement
from package.models import Package


class PackageView(View):
    template_name = 'package/package_advertisement.html'

    def get(self, request, package_pk, advertisement_pk):
        package = Package.objects.get(pk=package_pk)
        advertisement = Advertisement.objects.get(pk=advertisement_pk)
        return render(request, self.template_name, {'package': package, 'advertisement': advertisement})

    def post(self, request, package_pk, advertisement_pk):
        # purchase = Purchase.create(package, request.user)
        # return render(request, 'purchase/purchase_detail.html', context={})
        pass