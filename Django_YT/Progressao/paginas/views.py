from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

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

def TodoCreate(request):
    todos = Todo.objects.filter()
    return render(request, "todos/lista_todo.html")