from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #exsentar 
#from json import loads,dumps
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

@csrf_exempt
def division(request):
    a = request.POST['a']
    b = request.POST['b']
    #c = int(a)/int(b)
    return HttpResponse("La division de "+a+"/"+b+" = ")
    #return HttpResponse("Division")+ str(c)