from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'task'

urlpatterns = [
    path('',login_required(views.IndexView.as_view(), login_url='auth_system:login'), name='index'),
    path('task/add/', login_required(views.CreateTask.as_view(), login_url='auth_system:login'), name='add_task'),
    path('task/details/<int:pk>/', login_required(views.SingleView.as_view(), login_url='auth_system:login'), name='single'),
    path('task/update/<int:pk>/', login_required(views.UpdateTask.as_view(), login_url='auth_system:login'), name='update_task'),
    path('task/delete/<int:pk>/', login_required(views.DeleteTask.as_view(), login_url='auth_system:login'), name='delete_task'),
    
]