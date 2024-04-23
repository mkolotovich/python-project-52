from django.urls import path
from task_manager.tasks.models import Task
from task_manager.tasks.views import (
    TasksView,
    TaskFormCreateView,
    TaskFormEditView,
    TaskFormDeleteView,
    TaskFormView
)

urlpatterns = [
    path('', TasksView.as_view(model=Task), name='tasks'),
    path('create/', TaskFormCreateView.as_view(), name='new_task'),
    path('<int:pk>/update/', TaskFormEditView.as_view(), name='edit_task'),
    path('<int:pk>/delete/', TaskFormDeleteView.as_view(),
         name='drop_task'),
    path('<int:pk>/', TaskFormView.as_view(), name='view_task'),
]
