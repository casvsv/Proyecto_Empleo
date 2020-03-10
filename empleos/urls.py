from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('apps.modelo.urls')),
    path('persona/', include('apps.persona.urls'), name='persona'),
    path('login/', include('apps.login.urls'), name='login'),
    path('', views.homePage, name='home_page'),
    path('logout', views.cerrar, name='cerrar_sesion'),
]
