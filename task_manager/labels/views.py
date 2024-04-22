from django.shortcuts import render, redirect
from django.views import View
from .forms import LabelCreationForm
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin


class LabelsView(LoginRequiredMixin, View):
    def get(self, request):
        labels = Label.objects.all()
        return render(request, 'labels/index.html', context={'labels': labels})


class LabelFormCreateView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'form': LabelCreationForm()
        }
        return render(request, 'labels/new.html', context)

    def post(self, request):
        form = LabelCreationForm(request.POST)
        if form.is_valid():
            form.save()
            label_created = gettext("label_created")
            messages.add_message(request, messages.SUCCESS, label_created)
            return redirect('labels')
        context = {
            'form': form
        }
        return render(request, 'labels/new.html', context)


class LabelFormEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelCreationForm(instance=label)
        return render(request, 'labels/edit.html',
                      {'form': form, 'label_id': label_id, 'label': label})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelCreationForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            label_edit = gettext("label_edit")
            messages.add_message(request, messages.SUCCESS, label_edit)
            return redirect('labels')
        return render(request, 'labels/edit.html',
                      {'form': form, 'task_id': label_id})


class LabelFormDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        return render(request, 'labels/delete.html',
                      {'label': label, 'label_id': label_id})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        task = Task.objects.filter(labels=label_id)
        if task:
            messages.add_message(request, messages.ERROR,
                                 gettext("remove_label_error"))
            return redirect('labels')
        if label:
            label.delete()
            label_remove = gettext("label_remove")
            messages.add_message(request, messages.SUCCESS, label_remove)
            return redirect('labels')
