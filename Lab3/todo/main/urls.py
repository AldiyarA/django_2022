from django.urls import path

from main.views import *

urlpatterns = [
    path('<int:list_id>/', TaskListAPIView.as_view()),
    path('<int:list_id>/completed/', CompletedTaskListAPIView.as_view()),
    path('tasks/', TasksAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
]