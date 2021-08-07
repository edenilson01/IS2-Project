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
    path('error/', control.logeado),
    path('home/', control.home),
    path('proyectos/', control.proyectos),
]

urlpatterns += staticfiles_urlpatterns()