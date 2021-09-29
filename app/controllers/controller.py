#aqui van los controladores, encargados de la logica del negocio
#se pueden agregar mas archivos

from django.urls.base import resolve
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import json

from sys import path as path
path.append('./')
from app.models.personas_model import PersonaModel
from app.models.proyectos_model import ProyectoModel
from app.models.permisos_model import PermisosModel
from app.models.usuarios_model import UserModel
from app.models.roles_model import RolesModel
from app.models.usuario_roles_model import UsuarioRolModel
from app.models.rol_permiso_model import RolPermisoModel

class ViewRequest:
    def __init__(self):
        self.usuario_logueado = None
        self.mensaje_error = []
        self.titulo_error = None
        self.id_proyecto = None

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
                self.usuario_logueado = usuario
                ids = self.obtener_roles_usuario(usuario)
                permisos = []
                if ids is not None:
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


        persona['id'] = PersonaModel().insert_persona(
            persona['p_nombre'],
            persona['s_nombre'],
            persona['p_apellido'],
            persona['s_apellido'],
            persona['fec_nac']
        )
        # usuario_model = UserModel()
        UserModel().insert_user(usuario['username'], usuario['password'], persona['id'], usuario['correo'])

        #TODO falta roles
  
        return redirect('/signup/')
    


    def modificar_usuario(self, request):
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
        usuario['username'] = request.GET['username2']
        usuario['correo'] = request.GET['correo']
        usuario['password'] = request.GET['password']
        print(usuario)

        modelo_usuario = UserModel()
        persona['id'] = modelo_usuario.consult_id_persona(usuario['username'])
        PersonaModel().update_persona(
            persona['p_nombre'],
            persona['s_nombre'],
            persona['p_apellido'],
            persona['s_apellido'],
            persona['fec_nac'],
            persona['id']
        )
        # usuario_model = UserModel()
        modelo_usuario.update_user(usuario['password'], usuario['correo'], usuario['username'])

        #TODO falta roles
  
        return redirect('/user_settings/')
    
    #def prueba(self, request):
    #    roles = request.GET.getlist('roles[]')
    #    usuario_rol = UsuarioRolModel()
    #    #for rol in roles:
    #    #    usuario_rol.insert_rol_usuario()
    #    return HttpResponse('Sucess')


    ###################################################

    def rol_nombre(self, request):
        return render(request, 'asignar_nombre_rol.html')

    def rol_permisos(self, request):
        return render(request, 'asignar_permisos.html')

    def modificar_rol(self, request):
        view = loader.get_template('modificar_rol.html')
        html_reponse = view.render({'lista_roles': self.obtener_roles()})
        return HttpResponse(html_reponse)

    def eliminar_rol(self, request):
        view = loader.get_template('delete_rol.html')
        html_reponse = view.render({'lista_roles': self.obtener_roles()})
        return HttpResponse(html_reponse)
        
    def seguridad(self, request):
        return render(request, 'seguridad.html')

    
    ################### MODIFICAR USUARIO
    def modificar_user(self, request):
        view = loader.get_template('modificar_user.html')
        html_reponse = view.render({'lista_roles': self.obtener_roles()})
        return HttpResponse(html_reponse)
    
    def obtener_usuario(self, request):
        username = request.GET.get('username')
        usuario = UserModel().consult_persona(username)
        if usuario is None:
            return HttpResponse(status=400) ##VER
        
        persona = PersonaModel().consult_per(usuario[2])
        datos_persona={}
        datos_persona['p_nombre'] = persona[1]
        datos_persona['s_nombre'] = persona[2]
        datos_persona['p_apellido'] = persona[3]
        datos_persona['s_apellido'] = persona[4]
        datos_persona['nacimiento'] = persona[5].strftime("%Y-%m-%d")
        datos_persona['correo'] = usuario[3]
        datos_persona['pass'] = usuario[1]
        datos_persona['permisos'] = self.obtener_roles_usuario(username)
        datos_persona['username'] = username

        return HttpResponse(json.dumps(datos_persona), content_type='application/json')
    
    def obtener_roles_usuario(self, usuario_user):
        return UsuarioRolModel().consult_id_roles(usuario_user)

            

    ######################### ELIMINAR USUARIO    
    def eliminar_user(self, request):
        return render(request, 'delete_user.html')

    def del_user(self, request):
        usuario = request.GET['username2']
        UserModel().delete_user(usuario)
        return redirect('/delete_user/')  

    def buscar_user_elm(self, request):
        username = request.GET.get('username')
        usuario = UserModel().consult_persona(username)

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
        datos_persona['username'] = username
        return HttpResponse(json.dumps(datos_persona), content_type='application/json')


    
    ################################PERMISOS
    def crear_permisos(self, request):
        return render(request, 'crear_permiso.html')

    def reg_permiso(self, request):
        nombre = request.GET['nombre_permiso']
        descripcion = request.GET['desc_permiso']
        PermisosModel().insert_permiso(nombre, descripcion)
        return redirect('/crear_permiso/')

    def modificar_permisos(self, request):
        view = loader.get_template('modificar_permiso.html')
        html_reponse = view.render({'lista_permisos': self.obtener_permisos()})
        return HttpResponse(html_reponse)

    def eliminar_permisos(self, request):
        view = loader.get_template('eliminar_permiso.html')
        html_reponse = view.render({'lista_permisos': self.obtener_permisos()})
        return HttpResponse(html_reponse)
        
    def obt_permiso(self, request):
        id_permiso = request.GET['id_permiso']
        campos_permiso = PermisosModel().consult_permiso_by_id(id_permiso)
        permiso = { 
            'nombre': campos_permiso[0], 
            'descripcion': campos_permiso[1],
            'id_permiso': id_permiso 
        }
        return HttpResponse(json.dumps(permiso), content_type='application/json')
    
    def mod_permiso(self, request):
        nuevo_nombre = request.GET['nombre']
        descripcion = request.GET['descripcion']
        id_permiso = request.GET['id_permiso']
        PermisosModel().update_permiso(nuevo_nombre, descripcion, id_permiso)
        return redirect('/modificar_permiso/')

    def del_permiso(self, request):
        PermisosModel().delete_permiso(request.GET['id_permiso'])
        return redirect('/eliminar_permiso/')  

    #############################PROYECTOS
    def proyecto(self, request):
        lista_proyectos = ProyectoModel().consult_proyectos()
        if lista_proyectos is None:
            print('No hay proyectos')
 
        view = loader.get_template('proyecto.html')
        html_reponse = view.render({'lista_proyectos': lista_proyectos})
        return HttpResponse(html_reponse)
    
    def guardar_proyecto_id(self, request):
        self.id_proyecto = request.GET['id_proyecto']
        return HttpResponse()

    def modificar_proyecto(self, request):
        return render(request, 'modificar_proyecto.html')

    def mod_proyecto(self, request):
        nuevo_nombre = request.GET['proy_nombre']
        if request.GET.get('estado') is None:
            estado = False
        else:
            estado = True

        if nuevo_nombre == '':
            ProyectoModel().update_estado_fin(estado, self.id_proyecto)
        else:
            ProyectoModel().update_project(nuevo_nombre, estado, self.id_proyecto)
            
        return render(request, 'modificar_proyecto.html')

    def crear_proyecto(self, request):
        return render(request, 'crear_proyecto.html')

    def reg_proyecto(self, request):
        ProyectoModel().insert_project(request.GET['pro_nombre'])
        return render(request, 'crear_proyecto.html')
    
    def del_proyecto(self, request):
        ProyectoModel().delete_project(request.GET['id_proyecto'])
        return HttpResponse()

    def equipo(self, request):
        return render(request, 'equipo.html')

    def add_miembro(self, request):
        return render(request, 'add_miembro.html')
    
    def delete_miembro(self, request):
        return render(request, 'delete_miembro.html')
    
    def lista_miembro(self, request):
        return render(request, 'lista_miembro.html')

    #Desarrollo
    def desarrollo(self, request):
        return render(request, 'desarrollo.html')


    ##otras funciones
    def obtener_roles(self):
        return RolesModel().consult_roles()

    def obtener_permisos(self):
        return PermisosModel().consult_permiso()
