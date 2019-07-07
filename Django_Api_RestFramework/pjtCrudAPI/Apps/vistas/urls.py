from django.urls import path, include

from Apps.vistas.views import *

urlpatterns = [
    path('', index, name="index"),
]
