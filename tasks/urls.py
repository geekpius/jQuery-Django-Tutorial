from django.urls import path
from .views import (TaskView, ViewTaskView, TaskUpdateDeleteView, TutorialView, TutorialDataView)

app_name = "tasks"

urlpatterns = [
    path('', TaskView.as_view(), name="task"), 
    path('view', ViewTaskView.as_view(), name="view"), 
    path('view/<int:pk>/', TaskUpdateDeleteView.as_view(), name="update_delete"), 
    
    path('tutorial', TutorialView.as_view(), name="tutorial"), 
    path('tutorial/data', TutorialDataView.as_view(), name="tutorial_data"), 
]