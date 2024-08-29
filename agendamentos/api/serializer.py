from rest_framework import serializers
from agendamentos.models import Agendamentos

class AgendamentosSerializer(serializers.ModelSerializer):  # Corrigido para ModelSerializer
    class Meta: 
        model = Agendamentos
        fields = '__all__'  # Corrigido para fields e removido o espaço extra
