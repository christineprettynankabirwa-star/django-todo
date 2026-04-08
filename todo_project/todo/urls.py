from django.urls import path
from .views import task_list, TasklistCreate, TaskUpdateDelete 

urlpatterns = [
    #HTML page
    path('', task_list, name='task_list'),

#API endpoints(DRF)
    path('api/tasks/', TaskListCreate.as_view() name='api_tasks'),
    path('api/tasks/<int:pk>/', TaskUpdateDelete.as_view() name='api_task_detail'),
] 
