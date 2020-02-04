from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [

    url(r'^persona$', views.PersonaList.as_view()),
    url(r'^persona/(?P<pk>[0-9]+)$', views.PersonaDetail.as_view()),
    url(r'^anuncio$', views.AnuncioList.as_view()),
    url(r'^anuncio/(?P<pk>[0-9]+)$', views.AnuncioDetail.as_view()),
    url(r'^postulacion$', views.PostulacionList.as_view()),
    url(r'^postulacion/(?P<pk>[0-9]+)$', views.PostulacionDetail.as_view()),
]
