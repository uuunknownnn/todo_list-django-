from django.urls import path
from .views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView
from . import views

urlpatterns = [
    path('', TodoListView.as_view(), name="home"),
    path('detail/<int:pk>/',TodoDetailView.as_view() , name="todo-detail"),
    path('new/', TodoCreateView.as_view(), name="todo-create"),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name="todo-update"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name="todo-delete"),
]


