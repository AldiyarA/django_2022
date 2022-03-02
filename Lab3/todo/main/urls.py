from django.urls import path

from main.views import todo_list, completed_todo_list

urlpatterns = [
    path('', todo_list),
    path('1/completed/', completed_todo_list),
]