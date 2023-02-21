from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('<h1> Hola desde Django</h1>')
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola '+ nombre)

def bienvenida(request):
    letrero = "Bienvenida"
    return HttpResponse(letrero)

def multiplicacion(request):
    p = request.GET['p']
    q = request.GET['q']
    r = int(p)*int(q)
    return HttpResponse("La multiplicacion de "+p+"x"+q+" = "+ str(r))

def division(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)/int(b)
    return HttpResponse("La multiplicacion de "+a+"x"+b+" = "+ str(c))