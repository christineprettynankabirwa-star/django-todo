from django.shortcuts import render
# Create your views here.
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/tasks.html', {'tasks': tasks})


