from django.urls import path
from rest_framework import routers

from main.views import *

# urlpatterns = [
#     path('<int:list_id>/', TaskListAPIView.as_view()),
#     path('<int:list_id>/completed/', CompletedTaskListAPIView.as_view()),
#     path('tasks/', TasksAPIView.as_view()),
#     path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
# ]

router = routers.DefaultRouter()
router.register('todo_lists', ToDoListViewSet)
router.register('todos', ToDoViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('todo_lists/<int:id>/todos/', list_todos),
]

