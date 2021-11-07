"""Inge2Grupo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sys import path as sys_path
sys_path.append('./')
from app.controllers.controller import ViewRequest


control = ViewRequest()

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', lambda request: redirect('login/', permanent=True)),
    path('login/', control.iniciar_sesion),
    path('working/', control.sitio_en_construccion),
    path('login_form/', control.logeado),

    path('home/', control.home),

    path('rol_nombre/', control.rol_nombre),
    path('rol_permisos/', control.rol_permisos),
    path('modificar_rol/', control.modificar_rol),

    path('seguridad/', control.seguridad),

    path('signup/', control.crear_usuario),
    path('reg_user/', control.registrar_usuario),
    path('mod_user/', control.modificar_usuario),
    path('guardar_roles_selected/', control.guardar_roles_selected),

    path('user_settings/', control.modificar_user),
    path('obtener_usuario/', control.obtener_usuario),

    path('delete_user/', control.eliminar_user),
    path('del_user/', control.del_user),
    path('obtener_usuario_elim/', control.buscar_user_elm),

    path('proyects/', control.proyecto),
    path('guardar_proyecto_id/', control.guardar_proyecto_id),
    path('modificar_proyecto/', control.modificar_proyecto),
    path('mod_proyecto/', control.mod_proyecto),
    path('reg_proyecto/', control.reg_proyecto),
    path('del_proyecto/', control.del_proyecto),
    
    path('crear_permiso/', control.crear_permisos),
    path('reg_permiso/', control.reg_permiso),
    path('obt_permiso/', control.obt_permiso),
    path('modificar_permiso/', control.modificar_permisos),
    path('mod_permiso/', control.mod_permiso),
    path('eliminar_permiso/', control.eliminar_permisos),
    path('del_permiso/', control.del_permiso),
    
    path('lista_miembro/', control.lista_miembro),
    path('add_miembro/', control.add_miembro),
    path('add_miembro_proyect/', control.add_miembro_proyect),
    path('delete_miembro/', control.delete_miembro),
    path('del_miembro/', control.del_miembro),


    path('delete_rol', control.eliminar_rol),
    
    #path('prueba/', control.prueba),
    
    path('crear_proyecto', control.crear_proyecto),
    path('equipo', control.equipo),
    path('add_miembro/', control.add_miembro),
    path('delete_miembro/', control.delete_miembro),
    path('lista_miembro/', control.lista_miembro),
    path('desarrollo/', control.desarrollo),
    path('crear_us/', control.crear_us),
    path('add_us/', control.add_us),

    path('desarrollo/', control.desarrollo),
    path('backlog/', control.backlog),
    path('eliminar_us/',control.eliminar_us),

    path('sprint/', control.sprint),
    path('crear_sprint/', control.crear_sprint),
    path('reg_sprint/', control.reg_sprint),
    path('fin_sprint/', control.fin_sprint),
    path('iniciar_sprint/', control.iniciar_sprint),
    path('calcular_fecha/', control.calcular_fecha_duracion_sprint),
    path('ini_sprint/', control.ini_sprint),
    path('existe_us/', control.comprobar_us_sprint),

    path('del_us_h', control.del_us_h),
    path('modificar_us/', control.modificar_us),
    path('mod_us/', control.mod_us),
    path('obt_us/', control.obt_us),    
    path('guardar_us_id/', control.guardar_us_id),

    path('modificar_sprint/', control.modificar_sprint),

    #path('agregar_us/', control.agregar_us),
    path('agregar_us/', control.agregar_us),
    path('add_incidencia/', control.add_incidencia),
    
    path('asignar_user/', control.asignar_user),
    path('guardar_sprint_id/', control.guardar_sprint_id),

    path('kanban/', control.kanban),
    path('kanban2/', control.kanban2),
    path('add_user_sprint/', control.add_user_sprint),
    path('update_state_us/', control.actualizar_estado_us)

]

urlpatterns += staticfiles_urlpatterns()