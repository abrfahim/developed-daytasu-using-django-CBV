from django.shortcuts import render
from task.models import Task, User
from rest_framework import generics, status
from .serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.
class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer