#from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import Profile
from Profile.models import modelOcupacion
from Profile.models import modelCiudad
from Profile.models import modelEstado
from Profile.models import modelEstado_Civil
from Profile.models import modelGenero
from Profile.serializer import ProfileSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import Estado_CivilSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import GeneroSerializers
from Profile.serializer import OcupacionSerializers

import coreapi
from rest_framework.schemas import AutoSchema

class ProfileLisViewSchema(AutoSchema):
    def get_manual_fields(self,path,method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('nombre')
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields
           

class ProfileList(APIView):
    permission_classes = []
    schema = ProfileLisViewSchema()

    def get(self,request,format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        serializer = ProfileSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileOcupacion(APIView):
    permission_classes = []
    schema = ProfileLisViewSchema()
    def get(self,request,format=None):
        print("Metodo get filter")
        queryset = modelOcupacion.objects.filter(delete = False)
        serializer = OcupacionSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileCiudad(APIView):
    permission_classes = []
    schema = ProfileLisViewSchema()
    def get(self,request,format=None):
        print("Metodo get filter")
        queryset = modelCiudad.objects.filter(delete = False)
        serializer = CiudadSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileEstado(APIView):
    permission_classes = []
    schema = ProfileLisViewSchema()
    def get(self,request,format=None):
        print("Metodo get filter")
        queryset = modelEstado.objects.filter(delete = False)
        serializer = EstadoSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileEstado_Civil(APIView):
    permission_classes = []
    schema = ProfileLisViewSchema()
    def get(self,request,format=None):
        print("Metodo get filter")
        queryset = modelEstado_Civil.objects.filter(delete = False)
        serializer = Estado_CivilSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = Estado_CivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileGenero(APIView):
    permission_classes = []
    schema = ProfileLisViewSchema()
    def get(self,request,format=None):
        print("Metodo get filter")
        queryset = modelGenero.objects.filter(delete = False)
        serializer = GeneroSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)