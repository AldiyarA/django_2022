from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return f'ID-{self.pk} : {self.name}'


class Task(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    created = models.DateTimeField()
    due = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    mark = models.BooleanField(default=False)

    def __str__(self):
        return f'ID-{self.pk} : '

    def list__name(self):
        return self.list.name
