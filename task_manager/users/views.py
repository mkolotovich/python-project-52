from django.shortcuts import render, redirect
from django.views import View
from .forms import (
    UserCreationForm, CustomUserChangeForm, CustomSetPasswordForm)
from task_manager.users.models import User
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        # return render(request, 'welcome/index.html')
        a = None
        a.hello()
        return HttpResponse("Hello, world. You're at the pollapp index.")


class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/index.html', context={'users': users})


class UsersFormCreateView(View):
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context)


class UsersFormEditView(View):
    def get(self, request, *args, **kwargs):
        if (not request.user.is_authenticated):
            auth_error = gettext("auth_error")
            messages.add_message(request, messages.ERROR, auth_error)
            return redirect('login')
        if request.user.id != kwargs.get('pk'):
            edit_error = gettext("edit_error")
            messages.add_message(request, messages.ERROR, edit_error)
            return redirect('users')
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        user_form = CustomUserChangeForm(instance=user)
        pass_form = CustomSetPasswordForm(user)
        return render(request, 'users/edit.html',
                      {'form': user_form, 'password_form': pass_form,
                       'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        user_form = CustomUserChangeForm(request.POST, instance=user)
        password_form = CustomSetPasswordForm(user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            return redirect('users')
        return render(request, 'users/edit.html',
                      {'form': user_form, 'password_form': password_form,
                       'user_id': user_id})


class UsersFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html',
                      {'user': user, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        author = Task.objects.filter(author_id=user_id)
        executor = Task.objects.filter(executor_id=user_id)
        if author or executor:
            messages.add_message(request, messages.ERROR,
                                 gettext("remove_error"))
            return redirect('users')
        if user:
            user.delete()
            return redirect('users')
