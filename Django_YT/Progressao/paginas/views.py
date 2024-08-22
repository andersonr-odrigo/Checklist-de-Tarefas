from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, "home.html")

''''def lista_todo(request):
    todos = Todo.objects.all()
    return render(request, "todos/lista_todo.html", {"todos": todos})'''

class TodoListView(ListView):
    model = Todo