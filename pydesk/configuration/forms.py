'''
Created on Feb 6, 2014

@author: agoncalves
'''

from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, IntegerField
from configuration.models import Enterprise


class EnterpriseForm(ModelForm):
    id = IntegerField(widget=HiddenInput)
    
    class Meta:
        model = Enterprise
        fields = ('id', 'rasao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'endereco', 'observacao')
        widgets = {
            'rasao_social': TextInput(attrs={'size': 50}),
            'nome_fantasia': TextInput(attrs={'size': 50}),
            'cnpj': TextInput(attrs={'size': 20}),
            'inscricao_estadual': TextInput(attrs={'size': 20}),
            'endereco': TextInput(attrs={'size': 63}),
            'observacao': Textarea(attrs={'cols': 80, 'rows': 4}),
        }
        labels = {
            'rasao_social': _('Corporate Name'),
            'nome_fantasia': _('Fantasy Name'),
            'cnpj': _('CNPJ'),
            'inscricao_estadual': _('State Registration'),
            'endereco': _('Address'),
            'observacao': _('Observation'),
        }