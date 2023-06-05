from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_view(request):
    project = Project.objects.all()
    context = {
        "project": project
    }
    return render(request, "projects/all_projects.html", context)
