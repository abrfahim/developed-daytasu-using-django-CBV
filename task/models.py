from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=100, unique=True)
    due_date = models.DateTimeField()
    image = models.ImageField(upload_to='uploads/images', default='default_man.jpg', blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('task:single', args=[self.pk])
    
    class Meta:
        ordering=['-title', '-due_date', '-priority', '-is_completed']
    
    def __str__(self):
        return self.title
