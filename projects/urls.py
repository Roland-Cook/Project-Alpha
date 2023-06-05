from projects.views import project_view
from django.urls import path


urlpatterns = [
    path("", project_view, name="list_projects")
]
