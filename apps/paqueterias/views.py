from django.shortcuts import render
from django.views.generic import ListView
from apps.paqueterias.models import Paqueteria
# Create your views here.
class IndexView(ListView):
	template_name = 'paqueterias/index.html'
	model = Paqueteria
	
