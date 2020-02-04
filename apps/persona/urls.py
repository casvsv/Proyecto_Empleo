from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.principal, name="persona"),
    path('registrar_persona/', views.registrar_persona),
    path('anuncios/', views.mostrar_anuncios),
    path('anuncios/postular', views.postular),
    path('anuncios/crear_anuncio/', views.crear_anuncio),
]