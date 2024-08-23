from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="inicio"),
    path("lista_tarefas/", TodoListView.as_view(template_name="todos/lista_todo.html"), name="lista_tarefa"),
    path("create/", TodoCreate, name="criacao_tarefa"),
]
