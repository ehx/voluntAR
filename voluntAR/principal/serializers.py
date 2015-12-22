from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

class AccountSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Account

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer();
    class Meta:
        model = Account
