from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required


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
