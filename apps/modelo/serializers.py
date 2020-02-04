from rest_framework import serializers

from .models import Persona,Anuncio,Postulacion

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields =  ('persona_id','nombres','apellidos','fecha_nacimiento','celular','correo') 

class AnuncioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Anuncio
		fields =  ("anuncio_id","titulo","puesto","descripcion","area","pais","provincia","ciudad","direccion","persona")

class PostulacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Postulacion
		fields =  ("postulacion_id","salario","mensaje","persona","anuncio")

