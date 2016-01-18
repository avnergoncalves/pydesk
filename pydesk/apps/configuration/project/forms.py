# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, HiddenInput, TextInput, IntegerField

from pydesk.apps.configuration.project.models import Project


class ProjectForm(ModelForm):
    id = IntegerField(widget=HiddenInput(), required=False)
    
    class Meta:
        model = Project
        fields = ('id', 'description')
        widgets = {
            'description': TextInput(attrs={'size': 50}),
        }
        labels = {
            'description': _('Description'),
        }
