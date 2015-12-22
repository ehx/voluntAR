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
