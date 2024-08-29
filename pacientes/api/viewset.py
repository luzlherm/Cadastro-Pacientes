from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pacientes.models import Pacientes
from pacientes.api.serializer import PacientesSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer
    
    def  detalhes(self, request, pk=None, *args, **kwargs):