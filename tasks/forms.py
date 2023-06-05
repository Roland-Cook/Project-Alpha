from tasks.models import Task
from django.forms import ModelForm


class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "start_date", "due_date", "assignee", "project"]
