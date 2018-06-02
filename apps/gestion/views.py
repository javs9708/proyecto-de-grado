from apps.gestion.views import *
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

@login_required(login_url='/ingresar/')
def menu(request):
    if request.method == 'GET':
        username=None
        username=request.user.username
        usuario = User.objects.filter(username=username)


        template = loader.get_template('gestion/menu.html')
        ctx = {'usuario':usuario,
        }
        return HttpResponse(template.render(ctx,request))
