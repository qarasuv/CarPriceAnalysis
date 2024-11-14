from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

from core import settings

urlpatterns = [
    path("", include("car_pricing.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
