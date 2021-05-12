from django.urls import path
from tutorial.views import TutorialView, GetProductView

app_name = "tutorial"

urlpatterns = [
    path('', TutorialView.as_view(), name="index"), 
    path('<str:category>', GetProductView.as_view(), name="category"), 
]