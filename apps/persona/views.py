from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioAnuncio, FormularioModificarAnuncio, FormularioPersona, FormularioModificarPersona, FormularioPostulacion,FormularioModificarPostulacion
from apps.modelo.models import Persona, Anuncio, Postulacion
from django.contrib import messages


def principal(request):
	return render(request,'pagina_principal_sesion_iniciada.html')


def registrar_persona(request):
	formulario = FormularioPersona(request.POST)
	if request.method == 'POST':
		if formulario.is_valid():
			#Persona
			datos=formulario.cleaned_data #Obtener todos los datos del formulario
			persona=Persona() #Crea un objeto de la case Persona
			persona.nombres=datos.get('nombres')
			persona.apellidos=datos.get('apellidos')
			persona.fecha_nacimiento=datos.get('fecha_nacimiento')
			persona.correo=datos.get('correo')
			persona.celular=datos.get('celular')
			persona.save()
			mensaje = 'Se ha registrado correctamente'
			context = {
			'mensaje': mensaje
			}
			return render (request, 'status.html',context)
	context = {
		'formulario': formulario
	}
	return render(request, 'persona/registrar_persona.html', context)


def mostrar_anuncios(request):
	lista=Anuncio.objects.all()
	context={
		'lista': lista
	}
	return render(request,'anuncio/anuncios.html', context)

def crear_anuncio(request):
	formulario = FormularioAnuncio(request.POST)
	celu = request.GET['celular']
	persona = Persona.objects.get(celular = celu)
	if request.method == 'POST':
		if formulario.is_valid():
			#Persona
			datos=formulario.cleaned_data #Obtener todos los datos del formulario
			anuncio=Anuncio() #Crea un objeto de la case Persona
			anuncio.titulo=datos.get('titulo')
			anuncio.puesto=datos.get('puesto')
			anuncio.descripcion=datos.get('descripcion')
			anuncio.area=datos.get('area')
			anuncio.pais='Ecuador'
			anuncio.provincia=datos.get('provincia')
			anuncio.ciudad=datos.get('ciudad')
			anuncio.direccion=datos.get('direccion')
			anuncio.persona=persona
			anuncio.save()
			mensaje = 'Se ha creado el anuncio correctamente'
			context = {
			'mensaje': mensaje
			}
			return render (request, 'status.html',context)
	context = {
		'formulario': formulario
	}
	return render(request, 'anuncio/crear_anuncio.html', context)

def postular(request):
	formulario = FormularioPostulacion(request.POST)
	celu = request.GET['celular']
	persona = Persona.objects.get(celular = celu)
	if request.method == 'POST':
		id_a=request.GET['id']
		anuncio = Anuncio.objects.get(anuncio_id=id_a)
		if formulario.is_valid():
			#Persona
			datos=formulario.cleaned_data #Obtener todos los datos del formulario
			postulacion=Postulacion() #Crea un objeto de la case Persona
			postulacion.salario=datos.get('salario')
			postulacion.mensaje=datos.get('mensaje')
			postulacion.persona=persona
			postulacion.anuncio=anuncio
			postulacion.save()
			mensaje = 'Se ha postulado correctamente'
			context = {
			'mensaje': mensaje
			}
			return render (request, 'status.html',context)
	context = {
		'formulario': formulario
	}
	return render(request, 'postulacion/postular.html', context)