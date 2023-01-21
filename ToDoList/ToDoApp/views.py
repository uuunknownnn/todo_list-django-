from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo
# Create your views here.
#from ToDoApp import base
def home(request):
    todos = Todo.objects.all()
    return render(request, 'ToDoApp/base.html', {"todo_list": todos})


@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("home")

def update(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("home")

def delete(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect("home")