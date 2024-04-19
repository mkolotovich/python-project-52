from django.shortcuts import render, redirect
from django.views import View
from .forms import TaskCreationForm
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks/index.html', context={'tasks': tasks})


class TaskFormCreateView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'form': TaskCreationForm()
        }
        return render(request, 'tasks/new.html', context)

    def post(self, request):
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            task_created = gettext("task_created")
            messages.add_message(request, messages.SUCCESS, task_created)
            return redirect('tasks')
        context = {
            'form': form
        }
        return render(request, 'tasks/new.html', context)


class TaskFormEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskCreationForm(instance=task)
        return render(request, 'tasks/edit.html',
                      {'form': form, 'task_id': task_id, 'task': task})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            task_edit = gettext("task_edit")
            messages.add_message(request, messages.SUCCESS, task_edit)
            return redirect('tasks')
        return render(request, 'tasks/edit.html',
                      {'form': form, 'task_id': task_id})


class TaskFormDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        return render(request, 'tasks/delete.html',
                      {'task': task, 'task_id': task_id})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        if request.user.id != task.author_id:
            messages.add_message(request, messages.ERROR,
                                 gettext("remove_task_error"))
            return redirect('tasks')
        if task:
            task.delete()
            task_remove = gettext("task_remove")
            messages.add_message(request, messages.SUCCESS, task_remove)
            return redirect('tasks')


class TaskFormView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        return render(request, 'tasks/view.html',
                      {'task_id': task_id, 'task': task})