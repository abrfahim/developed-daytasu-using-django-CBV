from django.contrib import admin
from . models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'priority', 'is_completed']
    prepopulated_fields = {'slug':('title',),}
    list_filter = ('priority', 'is_completed', 'title')
    search_fields = ('title', 'description')
    
admin.site.register(Task, TaskAdmin)