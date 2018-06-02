from django.contrib import admin
from .models import *

@admin.register(Usuario)
class Usuario(admin.ModelAdmin):
    list_display = ['user','nombre_restaurante']
