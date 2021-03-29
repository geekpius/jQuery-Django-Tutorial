from django.urls import path
from .views import TaskView, ViewTaskView, TaskDeleteView

app_name = "tasks"

urlpatterns = [
    path('', TaskView.as_view(), name="task"), 
    path('view', ViewTaskView.as_view(), name="view"), 
    path('view/<int:pk>', TaskDeleteView.as_view(), name="delete"), 
]