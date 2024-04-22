from django.forms import ModelForm
from .models import Label
from django.utils.translation import gettext


class LabelCreationForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        labels = {
            "name": gettext("status_name"),
        }
