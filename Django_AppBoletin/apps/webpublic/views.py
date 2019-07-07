from django.shortcuts import render, redirect
from django.core import serializers
import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.webadmin.models import BoletinModelo
from apps.webpublic.serializers import BoletinSerializer

# Create your views here.

def home(request):
    return render(request, 'public/home.html')

class listar(ListView):
    model = BoletinModelo
    template_name = 'public/listar.html'

class detalle(DetailView):
    model = BoletinModelo
    template_name = 'public/detalle.html'

# ***************************************************************

# salida api con rest_framework.views
class BoletinAPI(APIView):
    serializers = BoletinSerializer

    def get(self, request, format=None):
        lista = BoletinModelo.objects.all()
        response = self.serializers(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')

def listaapi(request):
    return render(request, 'public/listaapi.html')

# ***************************************************************

#  salida json con serializar

def boletin_json(request):
    datos = BoletinModelo.objects.all()
    response_json = serializers.serialize('json', datos)
    return HttpResponse(response_json, content_type='application/json')

def listajson(request):
    return render(request, 'public/listajson.html')

