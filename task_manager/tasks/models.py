from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='author', null=True)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True)
    labels = models.ManyToManyField(Label, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
