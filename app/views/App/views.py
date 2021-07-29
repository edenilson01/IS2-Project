from django.shortcuts import render
from django.http import HttpResponse

def iniciar_sesion(request):
    return render(request, 'login.html')

def sitio_en_construccion(request):
    return render(request, 'construccion.html')

def logeado(request):
    correo = request.GET["usuario"]
    psw = request.GET["contrasena"]

    total = "CORREO: " + correo + ' CONSTRASEÑA: ' + psw

    return HttpResponse(total)