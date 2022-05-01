import os
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
ALLOWED_EXTENSIONS = ['.jpg', '.png']


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if ext.lower() not in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


class ToDoList(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return f'ID-{self.pk} : {self.name}'


class ToDo(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    due = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='todos')
    mark = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', validators=[validate_extension, ], null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='files/')

    def __str__(self):
        return f'ID-{self.pk} : {self.name}'

    def list__name(self):
        return self.list.name
