from django.shortcuts import render, redirect
from django.views import View
from .forms import StatusCreationForm
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import DeleteView, EditView, FormView


class StatusViewForm:
    value = Status
    template = 'index.html'


class StatusesView(LoginRequiredMixin, View, StatusViewForm, FormView):
    pass


class StatusesFormCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'new.html',
                      context={'form': StatusCreationForm()})

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


class StatusEditForm:
    value = Status
    template = 'edit.html'
    form = StatusCreationForm
    text = 'status_edit'
    path = 'statuses'


class StatusFormEditView(LoginRequiredMixin, View, StatusEditForm, EditView):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusCreationForm(instance=status)
        return render(request, 'edit.html',
                      {'form': form, 'status_id': status_id})
    pass


class StatusForm:
    value = Status
    template = 'delete.html'


class StatusFormDeleteView(LoginRequiredMixin, View, StatusForm, DeleteView):
    pass

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
