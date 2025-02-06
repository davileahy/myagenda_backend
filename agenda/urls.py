from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, TarefaViewSet, LembreteViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'tarefas', TarefaViewSet)
router.register(r'lembretes', LembreteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
