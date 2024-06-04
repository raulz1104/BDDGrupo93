from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Restaurant, Plato
from django.shortcuts import get_list_or_404

# Create your views here.
def hello(request):
    return render(request, 'index.html')

def show_restorants(request):
    print("Mostrando Restorants con plato...")
    plato = request.GET.get("plato")
    restaurants_id = map(lambda x: x.restaurante_id ,list(Plato.objects.get(nombre=plato)))
    restaurants = map(lambda x: Restaurant.objects.get(x), restaurants_id)
    return render(request, 'restorant.html',{
        'restaurants':restaurants
    })

def show_restorants_base(request):
    print("Mostrando Restorants...")
    restaurant = get_list_or_404(Restaurant)
    return render(request, 'platos.html')

def show_platos(request):
    print("Mostrando Platos...")
    return render(request, 'platos.html')