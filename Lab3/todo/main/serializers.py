from rest_framework import serializers
from main.models import ToDo, ToDoList


# class TaskListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ToDo
#         fields = ('name', 'owner', 'mark', 'list__name')


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoListSerializer(serializers.ModelSerializer):
    todos = ToDoSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'todos')

