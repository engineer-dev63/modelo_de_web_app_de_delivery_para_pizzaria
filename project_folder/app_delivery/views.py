from django.shortcuts import render
from django.http import HttpResponse
from .bd import PIZZAS #importing the 
# Create your views here.




def home(request):


    contexto = {
        'pizzas' : PIZZAS
    }

  
    return render(request, 'app_delivery/main/home.html' , contexto)


def menu(request):
    return render(request, 'app_delivery/main/menu.html')

def login(request):
    return render(request, 'app_deelivery/main/login.html')

def aboutus(request):
    return render(request, 'app_delivery/main/aboutus.html')



def estoque(request):
    termo_busca = request.GET.get('query', '').strip()

    if termo_busca:
        pizzas_filtradas = [
            pizza for pizza in PIZZAS

            if termo_busca.lower() in pizza['nome'].lower()
        
        ]
    else:
        pizzas_filtradas = PIZZAS
    
    return render(request, 'app_delivery/main/home.html', {'pizzas': pizzas_filtradas})






