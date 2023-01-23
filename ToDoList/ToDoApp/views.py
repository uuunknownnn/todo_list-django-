from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Todo


"""
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

"""

# CBV
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class TodoListView(ListView):
    model = Todo
    template_name = 'ToDoApp/home.html'
    context_object_name = 'todo_list'
    ordering = ["-date_posted"]


#overriding the get_context_data function to add more context:
    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        return context


"""
    class meta:
        fields = ["title", "complete", "date_posted"]
"""


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'ToDoApp/todo_detail.html'

    def get_absolute_url(self):
            return reverse('todo-detail',
               kwargs={'pk': self.pk })


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "complete", "content"]
   # success_url = '/'  <<<<------- this would redirect the browser to home page after a new post is created

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "content"]
    success_url = '/'

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = '/'