from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Evento, Tarefa, Lembrete
from .serializers import EventoSerializer, TarefaSerializer, LembreteSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas os eventos do usuário autenticado
        return self.queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # Define o usuário automaticamente ao criar um evento
        serializer.save(usuario=self.request.user)

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class LembreteViewSet(viewsets.ModelViewSet):
    queryset = Lembrete.objects.all()
    serializer_class = LembreteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
