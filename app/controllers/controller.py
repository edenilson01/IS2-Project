#aqui van los controladores, encargados de la logica del negocio
#se pueden agregar mas archivos

from django import http
from app.models.personas_model import PersonaModel
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import json

from sys import path as path
path.append('./')
from app.models.usuarios_model import UserModel
from app.models.roles_model import RolesModel
from app.models.usuario_roles_model import UsuarioRolModel
from app.models.rol_permiso_model import RolPermisoModel

class ViewRequest:
    def __init__(self):
        self.usuario_logueado = None
        self.mensaje_error = []
        self.titulo_error = None

    def enviar_sms_error(self, templade):        
        view = loader.get_template(templade)
        html_reponse = view.render({'titulo': self.titulo_error, 'errors': self.mensaje_error})

        self.mensaje_error = []
        return HttpResponse(html_reponse)

    ############################LOGIN
    def iniciar_sesion(self, request):
        return render(request, 'login.html')

    def sitio_en_construccion(self, request):
        return render(request, 'construccion.html')

    def logeado(self, request):
        modelo = UserModel()
        usuario = request.GET["usuario"]
        psw = request.GET["contrasena"]

        base_password = modelo.consult_persona(usuario)
        if base_password is not None:
            if base_password[1] == psw:
                ids = UsuarioRolModel().consult_id_roles(usuario)
                permisos = []
                for id in ids:
                    rol_permisos = RolPermisoModel().consult_permisos(id)
                    if rol_permisos is not None:
                        for per in rol_permisos:
                            permisos.append(per[0])

                view = loader.get_template('home.html')
                html = view.render({'user': self.usuario_logueado, 'permisos': permisos})
                return HttpResponse(html)

        #sino redirecciona, entonces es un error de credenciales
        self.titulo_error = 'Credenciales Inválidas'
        self.mensaje_error.append('El nombre de usuario y/o la contraseña que ingresaste no coinciden con nuestros registros.')
        self.mensaje_error.append('Por favor, revisa e inténtalo de nuevo.')

        return self.enviar_sms_error('login.html')  

    def home(self, request):
        view = loader.get_template('home.html')
        html = view.render({'user': self.usuario_logueado})
        return HttpResponse(html)

    def proyectos(self, request):
        view = loader.get_template('proyectos.html')
        html = view.render({'user': self.usuario_logueado})
        return HttpResponse(html)

    ##################################CREAR USUARIO
    def crear_usuario(self, request):
        view = loader.get_template('signup.html')
        html_reponse = view.render({'lista_roles': self.obtener_roles()})
        return HttpResponse(html_reponse)

    

    def registrar_usuario(self, request):
        #persona
        persona = {}
        persona['p_nombre'] = request.GET['p_nombre']
        persona['s_nombre'] = request.GET['s_nombre']
        persona['p_apellido'] = request.GET['p_apellido']
        persona['s_apellido'] = request.GET['s_apellido']
        persona['fec_nac'] = request.GET['fec_nacimiento']
        print(persona)
        #usuario
        usuario = {}
        usuario['username'] = request.GET['username']
        usuario['correo'] = request.GET['correo']
        usuario['password'] = request.GET['password']
        usuario['password2'] = request.GET['password_rep']
        print(usuario)

        if usuario['password'] != usuario['password2']:
            self.titulo_error = 'Error contraseñas'
            self.mensaje_error.append('No se verifican las contraseñas.')
            return self.enviar_sms_error('signup.html')


        # persona_model = PersonaModel()
        # persona['id'] = persona_model.insert_persona(
        #     persona['p_nombre'],
        #     persona['s_nombre'],
        #     persona['p_apellido'],
        #     persona['s_apellido'],
        #     persona['fec_nac']
        # )
        # usuario_model = UserModel()
        # usuario_model.insert_user(usuario['username'], usuario['password'], persona['id'])

        #roles
  
        return redirect('/signup/')
    
    def prueba(self, request):
        roles = request.GET.getlist('roles[]')
        usuario_rol = UsuarioRolModel()
        print(roles)
        #for rol in roles:
        #    usuario_rol.insert_rol_usuario()
        return HttpResponse('Sucess')


    ###################################################

    def rol_nombre(self, request):
        return render(request, 'asignar_nombre_rol.html')

    def rol_permisos(self, request):
        return render(request, 'asignar_permisos.html')

    def modificar_rol(self, request):
        return render(request, 'modificar_rol.html')
        
    def seguridad(self, request):
        return render(request, 'seguridad.html')

    
    ################### MODIFICAR USUARIO
    def modificar_user(self, request):
        view = loader.get_template('modificar_user.html')
        html_reponse = view.render({'lista_roles': self.obtener_roles()})
        return HttpResponse(html_reponse)
    
    def obtener_usuario(self, request):
        usuario = UserModel().consult_persona(request.GET.get('username'))
        if usuario is None:
            self.titulo_error = "ERROR"
            self.mensaje_error.append("No existe ese usuario")
            return HttpResponse(self.enviar_sms_error('modificar_user.html'), status=400) ##VER
        
        persona = PersonaModel().consult_per(usuario[2])
        datos_persona={}
        datos_persona['p_nombre'] = persona[1]
        datos_persona['s_nombre'] = persona[2]
        datos_persona['p_apellido'] = persona[3]
        datos_persona['s_apellido'] = persona[4]
        datos_persona['nacimiento'] = persona[5].strftime('%d/%m/%Y')
        datos_persona['correo'] = usuario[3]
        datos_persona['pass'] = usuario[1]

        return HttpResponse(json.dumps(datos_persona), content_type='application/json')
            

    ######################### ELIMINAR USUARIO    
    def eliminar_user(self, request):
        return render(request, 'delete_user.html')

    def buscar_user_elm(self, request):
        print(request.GET.get('username'))
        usuario = UserModel().consult_persona(request.GET.get('username'))
        print(usuario)
        if usuario is None:
            self.titulo_error = "ERROR"
            self.mensaje_error.append("No existe ese usuario")
            return HttpResponse(self.enviar_sms_error('modificar_user.html'), status=400) ##VER
        
        persona = PersonaModel().consult_per(usuario[2])
        datos_persona = {}
        pers = ''
        for ind in range(len(persona)):
            if persona[ind] is not None and ind > 0 and ind < 5:
                pers = pers + ' ' + str(persona[ind])

        datos_persona['nombre'] = pers
        datos_persona['correo'] = usuario[3]
        return HttpResponse(json.dumps(datos_persona), content_type='application/json')


    

    def crear_permisos(self, request):
        return render(request, 'crear_permiso.html')

    def modificar_permisos(self, request):
        return render(request, 'modificar_permiso.html')

    def eliminar_permisos(self, request):
        return render(request, 'eliminar_permiso.html')
        


    ##otras funciones
    def obtener_roles(self):
        return RolesModel().consult_roles()
