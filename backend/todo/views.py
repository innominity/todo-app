from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TodoTask
from .serializers import TodoTaskSerializer


@csrf_exempt
def get_tasks(request):
    tasks = TodoTask.objects.all()
    serializer = TodoTaskSerializer(tasks, many=True)
    return JsonResponse({'data': serializer.data})


@csrf_exempt
def create_task(request):
    title = request.POST.get("title")
    task = TodoTask.objects.create(title=title)
    serializer = TodoTaskSerializer(task, many=False)
    return JsonResponse({'task':serializer.data})


@csrf_exempt
def remove_task(request):
    task_id = int(request.POST.get('task_id'))
    TodoTask.objects.get(id=task_id).delete()
    return JsonResponse({'task_id': task_id})


@csrf_exempt
def update_task_status(request, task_id: int):
    task = TodoTask.objects.get(id = task_id)
    task_status = int(request.POST.get('task_status'))
    task.status = TodoTask.TodoTaskStatus.ACTIVE if task_status == 1 else TodoTask.TodoTaskStatus.DONE
    task.save()
    serializer = TodoTaskSerializer(task, many=False)
    return JsonResponse({'task': serializer.data})
