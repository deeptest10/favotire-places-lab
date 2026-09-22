from django.contrib import admin
from django.urls import path
from django.urls import include

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("places.urls")),
]