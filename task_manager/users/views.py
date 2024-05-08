from django.shortcuts import render, redirect
from django.views import View
from .forms import (
    UserCreationForm, CustomUserChangeForm, CustomSetPasswordForm)
from task_manager.users.models import User
from task_manager.tasks.models import Task
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.add_message(request, messages.INFO,
                             gettext("log_out"))
        return redirect('root')


class LoginView(View):
    def get(self, request):
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'registration/login.html', context)

    def post(self, request):
        form = AuthenticationForm(request.POST)
        context = {
            'form': form
        }
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 gettext("auth_success"))
            return redirect('root')
        else:
            messages.error(request, gettext("auth_form_error"))
            return render(request, 'registration/login.html', context)


class IndexView(View):
    def get(self, request):
        return render(request, 'welcome/index.html')


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
            messages.add_message(request, messages.SUCCESS,
                                 gettext("user_create_success"))
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
