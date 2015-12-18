from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'email', 'user_name', 'full_name')
    serializer_class = AccountSerializer
