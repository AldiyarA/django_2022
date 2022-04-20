from django.http import Http404
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Task, List
from main.serializers import TaskListSerializer, TaskDetailSerializer


# Create your views here.

def db():
    tasks = [
        {"name": "Task 0", "created": "10/09/2018", "due": "12/09/2018", "owner": "admin", "mark": "Done"},
        {"name": "Task 1", "created": "10/09/2018", "due": "12/09/2018", "owner": "admin", "mark": "Not Done"},
        {"name": "Task 2", "created": "10/09/2018", "due": "12/09/2018", "owner": "admin", "mark": "Not Done"},
        {"name": "Task 3", "created": "10/09/2018", "due": "12/09/2018", "owner": "admin", "mark": "Not Done"},
        {"name": "Task 4", "created": "10/09/2018", "due": "12/09/2018", "owner": "admin", "mark": "Not Done"}
    ]
    return tasks


class TaskListAPIView(APIView):

    def get(self, request, list_id):
        try:
            list = List.objects.get(pk=list_id)
        except List.DoesNotExist:
            raise Http404

        tasks = list.tasks
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class CompletedTaskListAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, list_id):
        try:
            list = List.objects.get(pk=list_id)
        except List.DoesNotExist:
            raise Http404

        tasks = list.tasks.filter(mark=True)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class TasksAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer