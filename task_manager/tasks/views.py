from django.shortcuts import render, redirect
from django.views import View

from task_manager.mixins import EditView
from .forms import TaskCreationForm, TaskFilter
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView


class TasksView(LoginRequiredMixin, FilterView):
    def get(self, request, *args, **kwargs):
        is_creator = False
        labels = request.GET.getlist('labels')
        status_id = request.GET.getlist('status')
        executor = request.GET.getlist('executor')
        if (request.GET.get('only_own_tasks')):
            tasks = TaskFilter(request.GET, queryset=Task.objects.all()
                               .filter(author_id=request.user.id))
            is_creator = True
        else:
            tasks = TaskFilter(request.GET, queryset=Task.objects.all())
        return render(request, 'tasks/task_filter.html',
                      {'filter': tasks, 'is_creator': is_creator,
                       'labels': labels, 'status_id': status_id,
                       'executor': executor})


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
            for label in form.cleaned_data['labels']:
                task.labels.add(label)
            task.save()
            task_created = gettext("task_created")
            messages.add_message(request, messages.SUCCESS, task_created)
            return redirect('tasks')
        context = {
            'form': form
        }
        return render(request, 'tasks/new.html', context)


class TaskForm:
    value = Task
    template = 'tasks/edit.html'
    form = TaskCreationForm
    text = 'task_edit'
    path = 'tasks'


class TaskFormEditView(LoginRequiredMixin, View, TaskForm, EditView):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        labels = task.labels.all().values_list('name')
        form = TaskCreationForm(instance=task)
        return render(request, 'tasks/edit.html',
                      {'form': form, 'task_id': task_id, 'task': task,
                       'labels': labels})
    pass


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
        labels = task.labels.all()
        return render(request, 'tasks/view.html',
                      {'task_id': task_id, 'task': task, 'labels': labels})
