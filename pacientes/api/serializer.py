from rest_framework import serializers
from pacientes.models import Pacientes
from agendamentos.api.serializer import AgendamentosSerializer

class PacientesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente',
            'nome',
            'rg',
            'data_nasc',
            'endereco',
            'num_endereco',
            'bairro',
            'cep',
            'data_cadastro',
            'agendamentos'
        ]
