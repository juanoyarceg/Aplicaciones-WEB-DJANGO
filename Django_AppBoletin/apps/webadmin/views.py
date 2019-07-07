from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.webadmin.models import BoletinModelo
from apps.webadmin.forms import BoletinForm

# Create your views here.

class boletin_listar(ListView):
	model = BoletinModelo
	template_name = 'private/boletin_listar.html'

class boletin_crear(CreateView):
	model = BoletinModelo
	form_class = BoletinForm
	template_name = 'private/boletin_crear.html'
	success_url = reverse_lazy('boletin_listar')

class boletin_editar(UpdateView):
	model = BoletinModelo
	form_class = BoletinForm
	template_name = 'private/boletin_editar.html'
	success_url = reverse_lazy('boletin_listar')

class boletin_eliminar(DeleteView):
	model = BoletinModelo
	template_name = 'private/boletin_eliminar.html'
	success_url = reverse_lazy('boletin_listar')
