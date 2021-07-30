#aqui van los controladores, encargados de la logica del negocio
#se pueden agregar mas archivos

from django.shortcuts import render
from django.http import HttpResponse

from sys import path as path
path.append('./')
from app.models.user_model import UserModel

class ViewRequest:
    def __init__(self):
        pass

    def iniciar_sesion(self, request):
        return render(request, 'login.html')

    def sitio_en_construccion(self, request):
        return render(request, 'construccion.html')

    def logeado(self, request):
        modelo = UserModel()
        usuario = request.GET["usuario"]
        psw = request.GET["contrasena"]

        base_password = modelo.consult_password(usuario)

        respuesta = ''
        if base_password is not None:
            if base_password == psw:
                respuesta = 'Bienvenido ' + usuario
            else:
                respuesta = 'Contraseña incorrecta'
        else:
            respuesta = 'No existe el usuario'

        return HttpResponse(respuesta)