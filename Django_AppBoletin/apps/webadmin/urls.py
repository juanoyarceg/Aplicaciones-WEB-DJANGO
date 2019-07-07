from django.urls import path,include

from apps.webadmin.views import *

urlpatterns = [
	path('', boletin_listar.as_view(),name = 'boletin_listar'),
	path('crear',boletin_crear.as_view(),name = 'boletin_crear'),
	path('editar/<int:pk>/',boletin_editar.as_view(),name = 'boletin_editar'),
	path('eliminar/<int:pk>/',boletin_eliminar.as_view(),name = 'boletin_eliminar'),
]