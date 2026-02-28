import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

class Proyecto:
    def __init__(self, nombre, autora):
        self.nombre = nombre
        self.autora = autora

def home(request):

    proyecto = Proyecto(
        nombre="Fundamentos de Linux e Introducción a Django",
        autora="Ali Vega"
    )

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + " PROBANDO CAMBIOS",
        "python_ver": os.environ["PYTHON_VERSION"] + " MAS CAMBIOS",        
        "project_name": proyecto.nombre,
        "project_author": proyecto.autora,
    }

    return render(request, "pages/home.html", context)