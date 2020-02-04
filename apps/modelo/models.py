from django.db import models


class Persona(models.Model):
	persona_id=models.AutoField(primary_key=True)
	nombres=models.CharField(max_length=50, null=False)
	apellidos=models.CharField(max_length=50, null=False)
	fecha_nacimiento=models.DateField(auto_now=False, auto_now_add=False, null=False)
	celular=models.CharField(max_length=10,unique=True)
	correo=models.EmailField(max_length=50,unique=True, null=False)

class Anuncio(models.Model):
	listaProvincia=(
		('Azuay','Azuay'),
		('Bolivar','Bolivar'),
		('Cañar','Cañar'),
		('Carchi','Carchi'),
		('Chimborazo','Chimborazo'),
		('Cotopaxi','Cotopaxi'),
		('El Oro','El Oro'),
		('Esmeraldas','Esmeraldas'),
		('Galápagos','Galápagos'),
		('Guayas','Guayas'),
		('Imbabura','Imbabura'),
		('Loja','Loja'),
		('Los Ríos','Los Ríos'),
		('Manabí','Manabí'),
		('Morona Santiago','Morona Santiago'),
		('Napo','Napo'),
		('Orellana','Orellana'),
		('Pastaza','Pastaza'),
		('Pichincha','Pichincha'),
		('Santa Elena','Santa Elena'),
		('Santo Domingo de los Tsachilas','Santo Domingo de los Tsachilas'),
		('Sucumbíos','Sucumbíos'),
		('Tungurahua','Tungurahua'),
		('Zamora Chinchipe','Zamora Chinchipe'),
	)
	anuncio_id=models.AutoField(primary_key=True)
	titulo=models.CharField(max_length=50, null=False)
	puesto=models.CharField(max_length=50, null=False)
	descripcion=models.TextField(max_length=500, null=False)
	area=models.CharField(max_length=50,null=False)
	pais=models.CharField(max_length=10, null=False)
	provincia=models.CharField(max_length=20, choices=listaProvincia, null=False)
	ciudad=models.CharField(max_length=20, null=False)
	direccion=models.CharField(max_length=20, null=False)
	persona=models.ForeignKey(
		'Persona',
		on_delete=models.CASCADE,
	)		

class Postulacion(models.Model):
	postulacion_id=models.AutoField(primary_key=True)
	salario=models.CharField(max_length=50, null=False)
	mensaje=models.TextField(max_length=500, null=False)
	persona=models.ForeignKey(
		'Persona',
		on_delete=models.CASCADE,
	)	
	anuncio=models.ForeignKey(
		'Anuncio',
		on_delete=models.CASCADE,
	)	