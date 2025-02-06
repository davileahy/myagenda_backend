from rest_framework import serializers
from .models import Evento, Tarefa, Lembrete

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = '__all__'
