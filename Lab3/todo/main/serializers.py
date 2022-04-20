from rest_framework import serializers
from main.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'owner', 'mark', 'list__name')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
