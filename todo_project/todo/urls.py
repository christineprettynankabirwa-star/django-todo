from django.urls import path
from .views import task_list, TasklistCreate, TaskUpdateDelete 

urlpatterns = [
    path('', task_list, name='task_list'),

    #API endpoints
    path('api/tasks/', TaskListCreate.as_view())
    path('api/tasks/<int:pk>/', TaskUpdateDelete.as_view()),
] 
