#aqui van los controladores, encargados de la logica del negocio
#se pueden agregar mas archivos

from django.shortcuts import render
from django.http import HttpResponse

class ViewRequest:
    def __init__(self):
        pass

    def iniciar_sesion(self, request):
        return render(request, 'login.html')

    def sitio_en_construccion(self, request):
        return render(request, 'construccion.html')

    def logeado(self, request):
        correo = request.GET["usuario"]
        psw = request.GET["contrasena"]

        total = "CORREO: " + correo + ' CONSTRASEÑA: ' + psw

        return HttpResponse(total)