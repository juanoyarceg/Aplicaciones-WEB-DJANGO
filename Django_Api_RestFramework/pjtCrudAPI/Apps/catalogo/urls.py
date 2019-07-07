from rest_framework import routers
from django.urls import path, include

from Apps.catalogo.views import CatalogoView

router = routers.DefaultRouter()
router.register("", CatalogoView)
urlpatterns = [
    path('', include(router.urls)),
]