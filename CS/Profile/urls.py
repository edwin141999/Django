from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Profile import views

urlpatterns = [
    re_path(r'Profile/$', views.ProfileList.as_view()),
    re_path(r'Profile/Estado_civil/$', views.ProfileEstado_Civil.as_view()),
    re_path(r'Profile/Ocupacion/$', views.ProfileOcupacion.as_view()),
    re_path(r'Profile/Genero/$', views.ProfileGenero.as_view()),
    re_path(r'Profile/Estado/$', views.ProfileEstado.as_view()),
    re_path(r'Profile/Ciudad/$', views.ProfileCiudad.as_view()),
]