from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('tasks', TaskListCreateView.as_view(), name='task_list_create'),
    path('tasks/<int:task_id>', TaskDetailView.as_view(), name='task_detail'),
   
]
