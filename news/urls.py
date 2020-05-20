from django.urls import path
from .views import listaNewsView,listaGiornalistiView
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista-articoli', listaNewsView.as_view(), name='lista_articoli'),
    path('lista-giornalisti', listaGiornalistiView.as_view(), name='lista_giornalisti'),

]