from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import home, demo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("demo/", demo, name='demo'),
] + static(settings.STATIC_URL)
