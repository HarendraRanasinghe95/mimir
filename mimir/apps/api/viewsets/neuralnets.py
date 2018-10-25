from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from keras.models import load_model

from ..serializers import NeuralNetSerializer
from ..models import NeuralNet
from .. import serializers

class NeuralNetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NeuralNetSerializer
    queryset = NeuralNet.objects.all()

    @action(methods=['post'], detail=True)
    def activate(self, request, pk=None):

        old = NeuralNet.objects.filter(active=True)

        if len(old) == 1:
            old[0].active = False
            old[0].save()

        new = NeuralNet.objects.get(pk=pk)
        new.active = True
        new.save()

        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def layers(self, request, pk=None):
        model = load_model(str(NeuralNet.objects.get(pk=pk).model_file))
        return Response([layer.name for layer in model.layers], status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=True)
    def classes(self, request, pk=None):
        classes = NeuralNet.objects.get(pk=pk).dataset.dataset_category_set.all()
        return Response(classes, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def predict(self, request, pk=None):
        pass