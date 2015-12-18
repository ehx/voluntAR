from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    #Ponemos los campos pass aca para que no sean obligatorios pasarlos, a menos que el usuario
    # quiera actualizar su pass.
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    # El resto de los campos los tomamos del model.
    # la subclase Meta define el metadata que el serializador necesita para operar.
    class Meta:
        model = Account     # como es ModelSerializer le decimos que modelo tomar.
        # Aca definimos que campos son serializados.
        fields = ('id', 'email', 'user_name', 'full_name', 'created_at',
                    'updated_at', 'password', 'confirm_password')
        read_only_fields = ('created_at', 'updated_at')

        #Definimos create y update para convertir un JSON en un objeto python.
        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            #Dejamos que actualize estos campos, si no viene en el validated_data tomamos el que ya esta.
            instance.user_name = validated_data.get('user_name', instance.user_name)
            instance.full_name = validated_data.get('full_name', instance.full_name)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            # por ahora uso este metodo para validar si cambio o no el pass. Ver si hay algo mejor
            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            #update_session_auth_hash(self.context.get('request'), instance)

            return instance
