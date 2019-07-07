from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('Apps.catalogo.urls')),
    path('vistas/', include('Apps.vistas.urls')),
]
