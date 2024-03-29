from django.shortcuts import render
from django.http import HttpResponse
from .models import proyecto
from django.views.decorators.csrf import csrf_exempt #exsentar 
from json import loads,dumps

class Fraccion:
    def __init__(self, num, den): #neceisto el numerador, y denominador
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)
# Create your views here.
def index(request):
    #return HttpResponse('<h1> Hola desde Django</h1>')
    return render(request, 'index.html')

def datos(request):
    jugadores = proyecto.objects.all()
    return render(request, 'datos.html', {'lista_jugadores':jugadores})

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request, 'proceso.html',{'name':nombre})
    return HttpResponse('Hola '+ nombre)

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num_resultado = num1 + num2
    den_resultado = den1 + den2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")


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
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    a = body['a']
    b = body['b']
    resultado = Fraccion(a,b)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")