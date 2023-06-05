from django.shortcuts import render
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
