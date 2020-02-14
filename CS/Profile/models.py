from django.db import models
from django.utils import timezone

# Create your models here.
#genero,ocupacion,estado civil
class modelEstado_Civil(models.Model):
    estado_civil = models.CharField(max_length=254, null=False)
    def __str__(self):
        return self.estado_civil

class modelOcupacion(models.Model):
    ocupacion = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.ocupacion    

class modelGenero(models.Model):
    sexo = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.sexo

class modelCiudad(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre

class modelEstado(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre


class Profile(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apPaterno = models.CharField(max_length=254, null=False)
    apMaterno = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(modelCiudad,on_delete=models.CASCADE)
    sexo = models.ForeignKey(modelGenero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(modelOcupacion,on_delete=models.CASCADE)
    estado = models.ForeignKey(modelEstado,on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(modelEstado_Civil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre,self.apMaterno,self.apMaterno,self.edad

    class Meta:
        db_table = 'Profile'