from django.shortcuts import render

from rest_framework import generics

from .models import Persona,Anuncio,Postulacion

from .serializers import PersonaSerializer,AnuncioSerializer,PostulacionSerializer

class PersonaList(generics.ListCreateAPIView):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer	

class AnuncioList(generics.ListCreateAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer

class AnuncioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer

class PostulacionList(generics.ListCreateAPIView):
	queryset = Postulacion.objects.all()
	serializer_class = PostulacionSerializer		

class PostulacionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Postulacion.objects.all()
	serializer_class = PostulacionSerializer			
