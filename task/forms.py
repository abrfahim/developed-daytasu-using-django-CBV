from django import forms
from .models import User, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'