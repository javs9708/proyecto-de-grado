from django.conf.urls import url, include
from apps.usuario.views import *



urlpatterns = [

                url(r'^registrar$',registrar, name='registrar'),

            ]
