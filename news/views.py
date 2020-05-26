from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Articolo,Giornalista
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, "home.html")

class listaArticoliView(ListView):
    model = Articolo
    template_name = 'news/articoli.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context

def listaArticoliGiornalistaView(request,pk):
    giornalista=get_object_or_404(Giornalista, id=pk)
    articoli=giornalista.articoli.all()
    context = {'giornalista': giornalista,
               'articoli': articoli,
               }
    return render(request, 'news/articoli.html', context)

class listaGiornalistiView(ListView):
    model = Giornalista
    template_name = 'news/giornalisti.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giornalisti"] = Giornalista.objects.all()
        return context