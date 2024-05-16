from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext


class FormView:
    def get(self, request):
        values = self.value.objects.all()
        return render(request, self.template, context={'values': values})


class DeleteView:
    def get(self, request, *args, **kwargs):
        value_id = kwargs.get('pk')
        value = self.value.objects.get(id=value_id)
        return render(request, self.template,
                      {'value': value, 'value_id': value_id})


class EditView:
    def post(self, request, *args, **kwargs):
        value_id = kwargs.get('pk')
        value = self.value.objects.get(id=value_id)
        form = self.form(request.POST, instance=value)
        if form.is_valid():
            form.save()
            value_edit = gettext(self.text)
            messages.add_message(request, messages.SUCCESS, value_edit)
            return redirect(self.path)
        return render(request, self.template,
                      {'form': form, 'value_id': value_id})
