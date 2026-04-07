from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import generics
from .models import Task
from.serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def task_list(request):
    if request.method == "POST":
        title = request.POST.get('title') 
        if title:
            Task.objects.create(title=title) 

        return redirect('task_list')
        
    tasks = Task.objects.all()
    return render(request, 'todo/tasks.html', {'tasks': tasks})


