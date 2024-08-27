from datetime import date

from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def home(request):
    return render(request, "home.html")

''''def lista_todo(request):
    todos = Todo.objects.all()
    return render(request, "todos/lista_todo.html", {"todos": todos})'''

class TodoListView(ListView):
    model = Todo

''' class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "data_criacao"]
    success_url = redirect("todos/lista_todo/")'''

class TodoCreateView(CreateView):
    model = Todo
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("lista_tarefa")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("lista_tarefa")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("lista_tarefa")

class TodoCompleteView(View):
    def get(self, request, pk):
        # Todo.objects.get(pk=pk)
        todo = get_object_or_404(Todo, pk=pk)
        todo.data_finalizacao = date.today()
        todo.save()
        return redirect("lista_tarefa")
