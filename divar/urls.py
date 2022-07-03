"""divar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from location.views import CitiesListView

urlpatterns = [
    # Home Page
    path('', CitiesListView.as_view(),),

    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('advertisement.urls')),
    path('financial/', include('financial.urls')),
    path('package/', include('package.urls')),
    path('purchase/', include('purchase.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
