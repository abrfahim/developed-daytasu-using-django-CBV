from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm


# Create your views here.

class IndexView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasklist'


class SingleView(DetailView):
    model = Task
    template_name = 'task/single_task.html'
    context_object_name = 'single_task'
    

class CreateTask(CreateView):
    model = Task
    template_name = 'task/add_task.html'
    fields = '__all__'
    success_url = reverse_lazy('task:index')
    
  
class UpdateTask(UpdateView):
    model = Task
    template_name = 'task/update_task.html'
    fields = '__all__'
    success_url = reverse_lazy('task:index')
    
    
class DeleteTask(DeleteView):
    model = Task
    template_name = 'task/confirm_delete.html'
    success_url = reverse_lazy('task:index')