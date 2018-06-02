from apps.usuario.views import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .funciones.validadores import *

def index(request):
    return render(request, 'usuario/index.html')

def ingresar(request):
    if request.method == 'GET':
        username=None
        username=request.user.username
        usuario = User.objects.filter(username=username).exists()
        if usuario:
            usuario = User.objects.get(username=username)
        if len(username)!=0 and not usuario.is_superuser:
            return redirect('/gestion/menu')

        template = loader.get_template('usuario/inicio.html')
        ctx = {
        }
        return HttpResponse(template.render(ctx,request))

    if request.method == 'POST':
        mensaje=(False,"")
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.filter(username=username).exists()
        if usuario:
            usuario = User.objects.get(username=username)
            if not usuario.is_superuser:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/gestion/menu')

                else:
                    mensaje = (True, "Contraseña invalida")
            else:
                mensaje = (True, "No existe el usuario " + username)
        else:
            mensaje = (True, "No existe el usuario " + username)


    template = loader.get_template('usuario/inicio.html')
    ctx = {'mensaje':mensaje,
            }
    return HttpResponse(template.render(ctx,request))

def registrar(request):
    if request.method == 'GET':
        username=None
        username=request.user.username
        usuario = User.objects.filter(username=username).exists()
        if usuario:
            usuario = User.objects.get(username=username)
        if len(username)!=0 and not usuario.is_superuser:
            return redirect('/gestion/menu')

        template = loader.get_template('usuario/registrar.html')
        ctx = {
        }
        return HttpResponse(template.render(ctx,request))



    if request.method == 'POST':
        mensaje = (False,"")

        username = request.POST.get('username')
        password1= request.POST.get('password1')
        password2= request.POST.get('password2')
        email = request.POST.get('email')
        nombre_restaurante = request.POST.get('nombre_restaurante')

        usuario = User.objects.filter(username=username).exists()
        correo = User.objects.filter(email=email).exists()
        if not usuario:
            if not correo:
                if password1 == password2:
                    user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password1
                            )
                    user.save()

                    usuario = Usuario.objects.create(
                            user = user,
                            nombre_restaurante = nombre_restaurante
                    )

                    usuario.save()

                    mensaje=(True,"Usuario registrado exitosamente")
                else:
                    mensaje=(True,"No coinciden las contraseñas")
            else:
                mensaje=(True,"Ya existe un usuario registrado con este correo")
        else:
            mensaje=(True,"Ya existe un usuario registrado con ese nombre de usuario")

    template = loader.get_template('usuario/registrar.html')
    ctx = {'mensaje':mensaje,
            }
    return HttpResponse(template.render(ctx,request))

@login_required(login_url='/ingresar/')
def cerrarSesion(request):
	if request.user is not None:
		logout(request)
	return redirect('index')
