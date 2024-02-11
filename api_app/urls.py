from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView

app_name = 'api_app'

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_create'),
]
