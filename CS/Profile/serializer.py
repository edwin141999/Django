from rest_framework import routers, serializers, viewsets

from Profile.models import Profile
from Profile.models import modelOcupacion
from Profile.models import modelCiudad
from Profile.models import modelEstado
from Profile.models import modelEstado_Civil
from Profile.models import modelGenero

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelEstado
        fields = ('__all__')

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelOcupacion
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelCiudad
        fields = ('__all__')

class Estado_CivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelEstado_Civil
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelGenero
        fields = ('__all__')