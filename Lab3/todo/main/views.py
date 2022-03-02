from django.http import HttpResponse
from django.shortcuts import render
from jinja2 import FileSystemLoader, Environment


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


def todo_list(request):
    fl = FileSystemLoader("main/templates/main")
    env = Environment(loader=fl)

    tm = env.get_template('todo_list.html')
    tasks = [i for i in db() if i['mark'] == "Not Done"]
    return HttpResponse(tm.render(todos=tasks))


def completed_todo_list(request):
    fl = FileSystemLoader("main/templates/main")
    env = Environment(loader=fl)

    tm = env.get_template('completed_todo_list.html')
    tasks = [i for i in db() if i['mark'] == "Done"]
    return HttpResponse(tm.render(todos=tasks))
