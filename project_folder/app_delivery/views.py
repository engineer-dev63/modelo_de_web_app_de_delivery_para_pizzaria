from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'app_delivery/main/home.html' )

def menu(request):
    return render(request, 'app_delivery/main/menu.html')

def login(request):
    return render(request, 'app_deelivery/main/login.html')

def aboutus(request):
    return render(request, 'app_delivery/main/aboutus.html')


def cards_dinamicos(request):
    pizzas = [
        {
            'nome': 'Calabresa especial',
            'descricao': 'Molho de tomate artesanal, mussarela premium e calabresa fatiada.',
            'preco': '45.00',
            'imagem': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500',
            'tag': 'Mais Pedida'
        }



    ]
    return render(request, 'carousel.html', {'pizzas': pizzas})