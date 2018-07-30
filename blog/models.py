# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone # Se añade esto segun tutrial djangogirls
# Create your models here.


#---------- Model 1 ----------- Post------------

class Post(models.Model): 
	# El modelo Post es una clase que hereda de la clase Model, asi se puede identificar como un modelo
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    # Autor es una propiedad del nuevo modelo post, almacenara el nombre del autor del post
    # es una llave foranea que indica que se vicula a otro modelo y su valor es unico
    title = models.CharField(max_length=200)
    # Almacena el titulo del post es del tipo char almacena un numero limitado de caracteres
    text = models.TextField()
    # Almacena el texto del post es del tipo text almacena un numero ilimitado de caracteres
    created_date = models.DateTimeField(
            default=timezone.now)
    # Almacena la fecha de creación del post el tipo de dato es datetime, y tiene un valor por defecto
    # que es timezone.now funcion importada desde la linea 6
    published_date = models.DateTimeField(
            blank=True, null=True)
    # Almaccena la fecha de publicacion del post y se asigna cuando se ejecuta el metodo publish definido en la linea 28
    def publish(self):
    	#Metodo que calculara el campo published_date
        self.published_date = timezone.now() 
        # la anterior variable ajustara la propiedad published_date
        self.save()
        # se guarda 

    def __str__(self):
    	# este constructor retornara el titulo del post
        return self.title