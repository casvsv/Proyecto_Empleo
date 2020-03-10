from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioAnuncio, FormularioModificarAnuncio, FormularioPersona, FormularioModificarPersona, FormularioPostulacion,FormularioModificarPostulacion
from apps.modelo.models import Persona, Anuncio, Postulacion
from django.contrib import messages


@login_required
def principal(request):
	usuario = request.user #Petición que es procesada por el framework y obtiene el usuario 
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
			color = 'success'
			mensaje_adicional='Porfavor inicie sesión'
			context = {
				'mensaje': mensaje,
				'color': color,
				'mensaje_adicional': mensaje_adicional,
			}
			return render (request, 'status.html',context)
	context = {
		'formulario': formulario
	}
	return render(request, 'persona/registrar_persona.html', context)

@login_required
def mostrar_anuncios(request):
	usuario = request.user #Petición que es procesada por el framework y obtiene el usuario 
	if usuario!='null':
		lista=Anuncio.objects.all()
		context={
			'lista': lista,
		}
		return render(request,'anuncio/anuncios.html', context)
	else:
		mensaje = 'No ha iniciado sesión aún'
		color = 'danger'
		mensaje_adicional='Porfavor inicie sesión'
		context = {
			'mensaje': mensaje,
			'color': color,
			'mensaje_adicional': mensaje_adicional,
		}
		return render(request,'status.html', context)

@login_required
def ver_postulaciones(request):
	usuario = request.user
	if usuario!='null':
		codigo = request.GET['codigo']
		anuncio=Anuncio.objects.get(anuncio_id=codigo)
		lista = Postulacion.objects.filter(anuncio_id = codigo)
		context={
			'lista': lista,
			'anuncio': anuncio.titulo,
		}
		return render(request,'postulacion/postulaciones.html', context)
	else:
		mensaje = 'No ha iniciado sesión aún'
		color = 'danger'
		mensaje_adicional='Porfavor inicie sesión'
		context = {
			'mensaje': mensaje,
			'color': color,
			'mensaje_adicional': mensaje_adicional,
		}
		return render(request,'status.html', context)		

@login_required
def buscar_anuncios(request):
	usuario = request.user
	if usuario!='null':
		consulta = request.GET['consulta']
		lista=Anuncio.objects.filter(titulo__contains=consulta).order_by('titulo')	
		if lista=='null':
			context={
				'mensaje': 'Lo sentimos, aún no hay empleos disponibles para ese campo',
				'color':'danger',
			}
		else:	
			context={
				'lista': lista
			}
		return render(request,'anuncio/anuncios.html', context)

@login_required
def crear_anuncio(request):
	usuario = request.user
	if usuario!='null':
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
				return render (request, 'anuncio/status_anuncio.html',context)
		context = {
			'formulario': formulario
		}
		return render(request, 'anuncio/crear_anuncio.html', context)


@login_required
def modificar_anuncio(request):
	usuario = request.user
	if usuario!='null':	
		anuncio_id = request.GET['id']
		anuncio = Anuncio.objects.get(anuncio_id = anuncio_id)
		if request.method == 'POST':
			formulario=FormularioModificarAnuncio(request.POST)
			if formulario.is_valid():
				datos=formulario.cleaned_data
				anuncio.titulo=datos.get('titulo')
				anuncio.puesto=datos.get('puesto')
				anuncio.descripcion=datos.get('descripcion')
				anuncio.area=datos.get('area')
				anuncio.pais='Ecuador'
				anuncio.provincia=datos.get('provincia')
				anuncio.ciudad=datos.get('ciudad')
				anuncio.direccion=datos.get('direccion')
				anuncio.save()
				mensaje = 'Se ha modificado el anuncio correctamente'
				context = {
				'mensaje': mensaje
				}
				return render (request, 'anuncio/status_anuncio.html',context)
		else:
			formulario=FormularioModificarAnuncio(instance = anuncio)
			context = {
				'anuncio': anuncio,
				'formulario': formulario,
			}
			return render(request, 'anuncio/modificar_anuncio.html', context)		


@login_required
def eliminar_anuncio(request):
	usuario = request.user
	if usuario!='null':	
		formulario = FormularioAnuncio(request.POST)
		anuncio_id = request.GET['id']
		anuncio = Anuncio.objects.get(anuncio_id = anuncio_id)
		anuncio.delete()
		mensaje = 'Se ha eliminado el anuncio correctamente'
		context = {
		'mensaje': mensaje
		}
		return render (request, 'anuncio/status_anuncio.html',context)


@login_required
def postular(request):
	usuario = request.user
	if usuario!='null':	
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
				return render (request, 'anuncio/status_anuncio.html',context)
		context = {
			'formulario': formulario
		}
		return render(request, 'postulacion/postular.html', context)