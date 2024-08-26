'''from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="inicio"),
    path("lista_tarefas/", TodoListView.as_view(), name="lista_tarefa"),
    path("", TodoCreateView.as_view(), name="criacao_tarefa"),
]'''