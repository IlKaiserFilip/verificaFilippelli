from django.shortcuts import render,HttpResponse
from django.views.generic.list import ListView
from .models import NewsArticoliModel,NewsGiornalistiModel

def index(request): 
    command_list = ['lista-articoli','lista-giornalisti']
    context = {
        'command_list': command_list,
    }
    return render(request, "home.html", context)

class listaNewsView(ListView):
    model = NewsArticoliModel  
    template_name = "news/articoli.html"

class listaGiornalistiView(ListView):
    model = NewsGiornalistiModel
    template_name = 'news/giornalisti.html'