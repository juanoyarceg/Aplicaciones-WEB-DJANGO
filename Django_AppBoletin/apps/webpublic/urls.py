from django.urls import path, include

from apps.webpublic.views import *

urlpatterns = [
	path('',home,name='home'),
	path('listar/', listar.as_view(),name='listar'),
	path('detalle/<int:pk>/', detalle.as_view(),name='detalle'),
	path('api/',BoletinAPI.as_view(),name='BoletinAPI'),
	path('listaapi/',listaapi,name='listaapi'),
	path('json/',boletin_json,name='boletin_json'),
	path('listajson',listajson,name='listajson'),
]
