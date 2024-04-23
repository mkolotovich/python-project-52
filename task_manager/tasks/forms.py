from django.forms import ModelForm
from .models import Task
from django.utils.translation import gettext
import django_filters


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            "name": gettext("status_name"),
            "description": gettext("task_description"),
            "status": gettext("status"),
            "executor": gettext("executor"),
            "labels": gettext("labels"),
        }


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
