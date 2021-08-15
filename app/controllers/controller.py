#aqui van los controladores, encargados de la logica del negocio
#se pueden agregar mas archivos

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from sys import path as path
path.append('./')
from app.models.usuarios_model import UserModel

class ViewRequest:
    def __init__(self):
        self.usuario_logueado = None
        self.mensaje_error = []
        self.titulo_error = None

    def iniciar_sesion(self, request):
        return render(request, 'login.html')

    def sitio_en_construccion(self, request):
        return render(request, 'construccion.html')

    def logeado(self, request):
        modelo = UserModel()
        usuario = request.GET["usuario"]
        psw = request.GET["contrasena"]

        base_password = modelo.consult_password(usuario)

        if base_password is not None:
            if base_password == psw:
                self.usuario_logueado = usuario
                return redirect('/home/')

        #sino redirecciona, entonces es un error de credenciales
        self.titulo_error = 'Credenciales Inválidas'
        self.mensaje_error.append('El nombre de usuario y/o la contraseña que ingresaste no coinciden con nuestros registros.')
        self.mensaje_error.append('Por favor, revisa e inténtalo de nuevo.')

        return self.enviar_sms_error()
    
    def enviar_sms_error(self):        
        view = loader.get_template('login.html')
        html_reponse = view.render({'titulo': self.titulo_error, 'errors': self.mensaje_error})

        self.mensaje_error = []
        return HttpResponse(html_reponse)
        

    def home(self, request):
        view = loader.get_template('home.html')
        html = view.render({'user': self.usuario_logueado})
        return HttpResponse(html)

    def proyectos(self, request):
        view = loader.get_template('proyectos.html')
        html = view.render({'user': self.usuario_logueado})
        return HttpResponse(html)

    def rol_nombre(self, request):
        return render(request, 'asignar_nombre_rol.html')

    def rol_permisos(self, request):
        return render(request, 'asignar_permisos.html')

    def modificar_rol(self, request):
        return render(request, 'modificar_rol.html')

    def eliminar_rol(self, request):
        return render(request, 'delete_rol.html')
        
    def seguridad(self, request):
        return render(request, 'seguridad.html')

    def registrar(self,request):
        return render(request, 'signup.html')

    def modificar_user(self, request):
        return render(request, 'modificar_user.html')
    
    def eliminar_user(self, request):
        return render(request, 'delete_user.html')
