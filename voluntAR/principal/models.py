from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", unique=True)
    logo = models.CharField(max_length=500, verbose_name="logo")
    is_ONG = models.BooleanField(default=False, verbose_name='ONG')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user.USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username

class Event(models.Model):
    owner = models.ForeignKey(Account, null=True, verbose_name='Propietario', related_name="accountEvent")
    finish_date = models.DateField(null=True, verbose_name='Fecha de Fin')
    picture = models.CharField(max_length=500, verbose_name="Imagen")
    title = models.CharField(max_length=50, verbose_name="Titulo")
    short_description = models.CharField(max_length=150, verbose_name="Descripcion Corta", blank=True)
    description = models.CharField(max_length=500, verbose_name="Descripcion", blank=True)
    #location = models.CharField()

    def __str__(self):
        return self.title

class Back(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.name

class BackElement(Back):
    quantity = models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        return self.name + ':' + str(self.quantity)

#Filtrar back_action para que no muestre elementos en las acciones

class EventVoluntary(models.Model):
    event = models.ForeignKey(Event, verbose_name="Evento")
    back_action = models.ManyToManyField(Back, related_name="Acciones_Voluntario")
    back_element = models.ManyToManyField(BackElement, related_name="Elementos_Voluntario")
    voluntary = models.ForeignKey(Account, verbose_name="Voluntario")
    comment = models.CharField(max_length=5000, verbose_name="Comentario")
    done = models.BooleanField(default=0, verbose_name="Realizado")

    def __str__(self):
        return self.voluntary.user.first_name + ' ' + self.event.title

class EventBack(models.Model):
    event = models.ForeignKey(Event, verbose_name="Evento")
    back_action = models.ManyToManyField(Back, related_name="Acciones_Evento")
    back_element = models.ManyToManyField(BackElement, related_name="Elementos_Evento")

    def __str__(self):
        return self.event.title
