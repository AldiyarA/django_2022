from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import ToDo, ToDoList
from main.serializers import ToDoSerializer, ToDoListSerializer


# Create your views here.

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = [IsAuthenticated]


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]


@api_view(["GET"])
def list_todos(request, id):
    if request.method == "GET":
        todos = ToDo.objects.filter(list=id)
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)
