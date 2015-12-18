from rest_framework import filters, status, permissions
from rest_framework import generics
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response



class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'email', 'user_name', 'full_name')
    serializer_class = AccountSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
