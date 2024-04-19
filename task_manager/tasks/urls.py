from django.urls import path
from task_manager.tasks import views
from task_manager.tasks.views import (
    TaskFormCreateView,
    TaskFormEditView,
    TaskFormDeleteView,
    TaskFormView
)

urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    path('create/', TaskFormCreateView.as_view(), name='new_task'),
    path('<int:pk>/update/', TaskFormEditView.as_view(), name='edit_task'),
    path('<int:pk>/delete/', TaskFormDeleteView.as_view(),
         name='drop_task'),
    path('<int:pk>/', TaskFormView.as_view(), name='view_task'),
]
