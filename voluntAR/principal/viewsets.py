from rest_framework import generics, filters
from rest_framework import viewsets
from .models import *
from .serializers import *

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

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  filter_backends = (filters.DjangoFilterBackend,)

  def get_serializer_class(self):
    # get one task
    if self.action == 'retrieve':
        return EventSerializer
    if self.action == 'list':
        return EventSerializer
    return EventSerializerWriter

class BackViewSet(viewsets.ModelViewSet):
  queryset = Back.objects.all()
  serializer_class = BackSerializer
  filter_backends = (filters.DjangoFilterBackend,)

class BackElementViewSet(viewsets.ModelViewSet):
  queryset = BackElement.objects.all()
  serializer_class = BackElementSerializer
  filter_backends = (filters.DjangoFilterBackend,)

class EventVoluntaryViewSet(viewsets.ModelViewSet):
  queryset = EventVoluntary.objects.all()
  serializer_class = EventVoluntarySerializer
  filter_backends = (filters.DjangoFilterBackend,)

class EventBackViewSet(viewsets.ModelViewSet):
  queryset = EventBack.objects.all()
  serializer_class = EventBackSerializer
  filter_backends = (filters.DjangoFilterBackend,)
