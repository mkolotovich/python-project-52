from django.shortcuts import render, redirect
from django.views import View
from task_manager.mixins import DeleteView, EditView, FormView
from .forms import LabelCreationForm
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin


class LabelsViewForm:
    value = Label
    template = 'labels/index.html'


class LabelsView(LoginRequiredMixin, View, LabelsViewForm, FormView):
    pass


class LabelFormCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'labels/new.html',
                      context={'form': LabelCreationForm()})

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


class LabelEditForm:
    value = Label
    template = 'labels/edit.html'
    form = LabelCreationForm
    text = 'label_edit'
    path = 'labels'


class LabelFormEditView(LoginRequiredMixin, View, LabelEditForm, EditView):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelCreationForm(instance=label)
        return render(request, 'labels/edit.html',
                      {'form': form, 'label_id': label_id, 'label': label})
    pass


class LabelForm:
    value = Label
    template = 'labels/delete.html'


class LabelFormDeleteView(LoginRequiredMixin, View, LabelForm, DeleteView):
    pass

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
