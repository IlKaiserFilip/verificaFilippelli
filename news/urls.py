from django.urls import path
from .views import listaArticoliView,listaGiornalistiView,listaArticoliGiornalistaView
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista-articoli', listaArticoliView.as_view(), name='lista_articoli'),
    path('lista-giornalisti', listaGiornalistiView.as_view(), name='lista_giornalisti'),
    path('lista-articoli-giornalista/<int:pk>', listaArticoliGiornalistaView, name='lista_articoli_giornalista'),

]