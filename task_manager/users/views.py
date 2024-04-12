from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from task_manager.users.models import User
from django.contrib import messages
from django.utils.translation import gettext


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
        form = UserCreationForm(instance=user)
        return render(request, 'users/edit.html',
                      {'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, 'users/edit.html',
                      {'form': form, 'user_id': user_id})


class UsersFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html',
                      {'user': user, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users')
