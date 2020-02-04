from django.contrib import admin
from .models import Persona,Anuncio,Postulacion

class AdminPersona(admin.ModelAdmin):
	list_display=["nombres","apellidos","fecha_nacimiento","celular","correo"]
	list_filter=["nombres","apellidos","fecha_nacimiento"]
	search_fields=["nombres","apellidos","fecha_nacimiento","celular","correo"]	
	class Meta:
		mode=Persona
admin.site.register(Persona, AdminPersona)

class AdminAnuncio(admin.ModelAdmin):
	list_display=["titulo","puesto","descripcion","area","pais","provincia","ciudad","direccion"]
	list_filter=["titulo","puesto","area","provincia","ciudad","direccion"]
	search_fields=["titulo","puesto","area","provincia","ciudad","direccion"]
	class Meta:
		mode=Anuncio
admin.site.register(Anuncio, AdminAnuncio)

class AdminPostulacion(admin.ModelAdmin):
	list_display=["salario","mensaje"]
	list_filter=["persona"]
	class Meta:
		mode=Postulacion
admin.site.register(Postulacion, AdminPostulacion)
