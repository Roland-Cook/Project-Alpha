from tasks.views import create_task, task_view
from django.urls import path

urlpatternss = [
    path("create/", create_task, name="create_task"),
    path("mine/", task_view, name="show_my_tasks"),
]
