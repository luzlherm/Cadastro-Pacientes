from rest_framework import viewsets
from agendamentos.models import Agendamentos
from agendamentos.api.serializer import AgendamentosSerializer  # Nome corrigido

class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
