from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models import NeuralNet
from .. import serializers

class NeuralNetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NeuralNetSerializer
    queryset = NeuralNet.objects.all()

    @action(methods=['post'], detail=True)
    def activate(self, request, pk=None):
        old = NeuralNet.objects.get(active=True)
        new = NeuralNet.objects.get(pk=pk)

        old.active = False
        new.active = True

        old.save()
        new.save()

    @action(methods=['get'], detail=True)
    def layers(self, request, pk=None):
        pass
    
    @action(methods=['get'], detail=True)
    def classes(self, request, pk=None):
        pass

    @action(methods=['get'], detail=True)
    def predict(self, request, pk=None):
        pass