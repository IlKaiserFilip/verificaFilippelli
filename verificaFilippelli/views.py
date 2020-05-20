from django.shortcuts import render

def index(request): 
    menu = ['news']
    context = {
        'menu': menu,
    }
    return render(request, "home.html", context)