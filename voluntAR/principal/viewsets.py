from rest_framework import generics, filters
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer, AccountSerializerWriter

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user', 'is_ONG')

    def get_serializer_class(self):
        # get one task
        if self.action == 'retrieve':
            return AccountSerializer
        if self.action == 'list':
            return AccountSerializer
        return AccountSerializerWriter
