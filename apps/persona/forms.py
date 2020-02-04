from django import forms
from apps.modelo.models import Anuncio, Persona, Postulacion

class FormularioAnuncio(forms.ModelForm):
	class Meta: 
		model = Anuncio
		fields =  ("titulo","puesto","descripcion","area","provincia","ciudad","direccion")


class FormularioModificarAnuncio(forms.ModelForm):
	class Meta: 
		model = Anuncio
		fields =  ("titulo","puesto","descripcion","area","provincia","ciudad","direccion")


class FormularioPersona(forms.ModelForm):
	class Meta: 
		model = Persona
		fields =  ('nombres','apellidos','fecha_nacimiento','celular','correo') 

class FormularioModificarPersona(forms.ModelForm):
	class Meta: 
		model = Persona
		fields =  ('nombres','apellidos','fecha_nacimiento','celular')


class FormularioPostulacion(forms.ModelForm):
	class Meta: 
		model = Postulacion
		fields =  ("salario","mensaje")

class FormularioModificarPostulacion(forms.ModelForm):
	class Meta: 
		model = Postulacion
		fields =  ("salario","mensaje")
