from django.shortcuts import render, redirect
from django.views import View
from .forms import StatusCreationForm
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusesView(LoginRequiredMixin, View):
    def get(self, request):
        statuses = Status.objects.all()
        return render(request, 'index.html', context={'statuses': statuses})


class StatusesFormCreateView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'form': StatusCreationForm()
        }
        return render(request, 'new.html', context)

    def post(self, request):
        form = StatusCreationForm(request.POST)
        if form.is_valid():
            form.save()
            status_created = gettext("status_created")
            messages.add_message(request, messages.SUCCESS, status_created)
            return redirect('statuses')
        context = {
            'form': form
        }
        return render(request, 'new.html', context)


class StatusFormEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusCreationForm(instance=status)
        return render(request, 'edit.html',
                      {'form': form, 'status_id': status_id})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusCreationForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            status_edit = gettext("status_edit")
            messages.add_message(request, messages.SUCCESS, status_edit)
            return redirect('statuses')
        return render(request, 'edit.html',
                      {'form': form, 'status_id': status_id})


class StatusFormDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        return render(request, 'delete.html',
                      {'status': status, 'status_id': status_id})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        task = Task.objects.filter(status_id=status_id)
        if task:
            messages.add_message(request, messages.ERROR,
                                 gettext("status_error"))
            return redirect('statuses')
        if status:
            status.delete()
            status_remove = gettext("status_remove")
            messages.add_message(request, messages.SUCCESS, status_remove)
            return redirect('statuses')
