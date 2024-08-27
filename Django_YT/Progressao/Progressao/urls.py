"""
URL configuration for Progressao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from paginas.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="pagina_inicial"),
    path("lista_tarefas/", TodoListView.as_view(template_name="todos/todo_list.html"), name="lista_tarefa"),
    path("create/", TodoCreateView.as_view(template_name="todos/todo_form.html"), name="criacao_tarefa"),
    path("update/<int:pk>", TodoUpdateView.as_view(template_name="todos/todo_form.html"), name="edicao_tarefa"),
    path("delete/<int:pk>", TodoDeleteView.as_view(template_name="todos/todo_confirm_delete.html"), name="deletar_tarefa"),
    path("complete/<int:pk>", TodoCompleteView.as_view(template_name="todos/todo_list.html"), name="finalizar_tarefa"),
]
