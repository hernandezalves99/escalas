from django.shortcuts import render 
from django.utils import timezone 
from .models import Evento 

def lista_escalas(request): 

    eventos = Evento.objects.filter(data__gte=timezone.now()) .order_by('data') 
    return render(request, 'escalas.html', {'eventos': eventos})

# Create your views here.
