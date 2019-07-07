from rest_framework import viewsets

from Apps.catalogo.models import CatalogoModelo
from Apps.catalogo.serializers import CatalogoSerialize

class CatalogoView(viewsets.ModelViewSet):
    queryset = CatalogoModelo.objects.all()
    serializer_class = CatalogoSerialize