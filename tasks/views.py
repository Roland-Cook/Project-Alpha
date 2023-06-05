from django.shortcuts import render, redirect
from tasks.forms import CreateTask
from django.contrib.auth.decorators import login_required
from tasks.models import Task


# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTask()
    context = {"form": form}
    return render(request, "tasks/create_tasks.html", context)


@login_required
def task_view(request):
    task = Task.objects.filter(assignee=request.user)
    context = {
        "task": task,
    }
    return render(request, "tasks/mine_tasks.html", context)
