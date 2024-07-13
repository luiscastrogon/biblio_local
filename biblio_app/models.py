from django.db import models

# Create your models here.

class navbaritem(models.Model):
    titulonav = models.CharField(max_length=10)
    url = models.CharField(max_length=20)

    def __str__(self):
        return str(self.titulonav)

class libro(models.Model):
    titulolib = models.CharField(max_length=100)
    aniopub = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=200)
        
    def __str__(self):
        return str(self.titulolib)

class autor(models.Model):
    nombreaut = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='static/images/', default='default.png')


    def __str__(self):
        return str(self.nombreaut)

class categoria(models.Model):
    nombrecat = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='static/images/', default='default.png')

    def __str__(self):
        return str(self.nombrecat)



