from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='admin:index', permanent=True)),
    path('admin/', admin.site.urls),  # isolate admin in case we add other apps
]
