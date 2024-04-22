from django.urls import path
from task_manager.labels import views
from task_manager.labels.views import (
    LabelFormCreateView,
    LabelFormEditView,
    LabelFormDeleteView,
)

urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels'),
    path('create/', LabelFormCreateView.as_view(), name='new_label'),
    path('<int:pk>/update/', LabelFormEditView.as_view(), name='edit_label'),
    path('<int:pk>/delete/', LabelFormDeleteView.as_view(),
         name='drop_label'),
]
