from django.urls import path
from .views import CommentView, CommentDataView

app_name = "comments"

urlpatterns = [
    path('', CommentView.as_view(), name="comment"), 
    path('/view', CommentDataView.as_view(), name="comment_data"), 
]