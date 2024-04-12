from django.urls import path
from task_manager.users import views
from task_manager.users.views import (
    UsersFormCreateView,
    UsersFormEditView,
    UsersFormDeleteView,
)

urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('create/', UsersFormCreateView.as_view(), name='new_user'),
    path('<int:pk>/update/', UsersFormEditView.as_view(), name='patch_user'),
    path('<int:pk>/delete/', UsersFormDeleteView.as_view(), name='drop_user'),
]
