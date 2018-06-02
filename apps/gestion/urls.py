from django.conf.urls import url, include
from apps.gestion.views import *



urlpatterns = [

                url(r'^menu$',menu, name='menu'),

            ]
