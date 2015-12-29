from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", unique=True)
    is_ONG = models.BooleanField(default=False, verbose_name='ONG')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user.USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.first_name  + ' ' + self.user.last_name

class Event(models.Model):
    owner = models.ForeignKey(Account, null=True, verbose_name='Propietario', related_name="accountEvent")
    finsh_date = models.DateField(null=True, verbose_name='Fecha de Fin')
    picture = models.CharField(max_length=500, verbose_name="Imagen")
    title = models.CharField(max_lenght=50, verbose_name="Titulo")
    short_description = models.CharField(max_length=150, verbose_name="Descripcion Corta", blank=True)
    description = models.CharField(max_length=500, verbose_name="Descripcion", blank=True)
    #location = models.CharField()
    actions = models.ArrayField(models.CharField(max_length=50), blank=True)
    elements = model.ArrayField({models.CharField(max_length=30), models.IntegerField}, blank=True) #¿?
    voluntaries = models.OneToManyField('Account')

    def __str__(self):
        return self.title
