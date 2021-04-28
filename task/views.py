from django.shortcuts import render
from django.views.generic import View
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

# Create your views here.


def get(request):
    tasks = list(Task.objects.all())

    final_list = []
    for task in tasks:
        final_list.append({"title": task.title, "iscompleted": task.completed})
    return JsonResponse({"tasks": final_list})


@csrf_exempt
def post(request):
    data = json.loads(request.body)
    task = Task(title=data["title"])
    task.save()
    return JsonResponse({"status": "success"})


@csrf_exempt
def delete(request):
    data = json.loads(request.body)
    task = Task.objects.get(title=data["title"])
    task.delete()
    return JsonResponse({"status": "sucess"})


@csrf_exempt
def markcompleted(request):
    data = json.loads(request.body)
    task = Task.objects.get(title=data["title"])
    task.completed = True

    task.save()
    return JsonResponse({"status": "sucess"})


@csrf_exempt
def delcomptasks(request):
    tasks = list(Task.objects.all())

    final_list = []
    for task in tasks:
        if task.completed:
            task.delete()
        else:
            final_list.append({"title": task.title, "iscompleted": task.completed})
    return JsonResponse({"tasks": final_list})