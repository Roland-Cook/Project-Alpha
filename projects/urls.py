from projects.views import project_view, project_detail
from django.urls import path


urlpatterns = [
    path("", project_view, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project")
]
