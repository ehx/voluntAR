from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class AccountManager(BaseUserManager):
    #Creamos un Manager para Account para poder redefinir el manejador de User.
    def create_user(self, email, password=None, **kwargs):
        # Redefinimos el metodo para crear usuarios de User.
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('user_name'):
            raise ValueError('Users must have a valid username.')

        account = self.model(email=self.normalize_email(email),
                            user_name=kwargs.get('user_name'))

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        # Redefinimos el metodo para crear super usuarios de User.
        account = self.create_user(email, password, **kwargs)
        account.is_admin=True
        account.save()

        return account

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=40, unique=True)

    full_name = models.CharField(max_length=150)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __unicode__(self):
        return self.email

    def getName(self):
        return self.full_name
