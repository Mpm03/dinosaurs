from rest_framework import viewsets
from .models import Dinosaur
from .serializers import DinosaurSerializer


class DinosaurViewSet(viewsets.ModelViewSet):
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
