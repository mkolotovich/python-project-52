from django.forms import ModelForm
from .models import Status
from django.utils.translation import gettext


class StatusCreationForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {
            "name": gettext("status_name"),
        }
