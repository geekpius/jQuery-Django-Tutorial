from django.urls import path
from .views import (TaskView, ViewTaskView, TaskUpdateDeleteView)

app_name = "tasks"

urlpatterns = [
    path('', TaskView.as_view(), name="task"), 
    path('view', ViewTaskView.as_view(), name="view"), 
    path('view/<int:pk>/', TaskUpdateDeleteView.as_view(), name="update_delete"), 
]