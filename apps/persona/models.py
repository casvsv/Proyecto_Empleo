from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioAnuncio,FormularioPersona,FormularioPostulacion
from apps.modelo.models import Anuncio, Persona, Postulacion
from django.contrib import messages