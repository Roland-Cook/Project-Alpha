from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import CreateProject

# Create your views here.


@login_required
def project_view(request):
    project = Project.objects.filter(owner=request.user)
    context = {
        "project": project
    }
    return render(request, "projects/all_projects.html", context)


@login_required
def project_detail(request, id):
    # recipe=Recipe.objects.get(id=id)
    project = get_object_or_404(Project.objects, id=id)
    context = {
        "project": project
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProject()
    context = {
        "form": form
            }
    return render(request, "projects/create.html", context)
