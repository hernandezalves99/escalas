from django.urls import path 
from .views import lista_escalas 

urlpatterns = [ 
path('escalas/', lista_escalas, name='lista_escalas'), ] 