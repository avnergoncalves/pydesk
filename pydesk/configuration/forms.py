'''
Created on Feb 6, 2014

@author: agoncalves
'''
from django import forms
from django.utils.translation import ugettext_lazy as _

class EnterpriseForm(forms.Form):
    rasao_social = forms.CharField(label=_("Corporate Name"), max_length=200, required=True)
    nome_fantasia = forms.CharField(label=_("Fantasy Name"), max_length=200, required=True)
    cnpj = forms.EmailField(label=_("CNPJ"), max_length=100, required=False)
    inscricao_estadual = forms.EmailField(label=_("State Registration"), max_length=100, required=False)
    endereco = forms.EmailField(label=_("Address"), max_length=100, required=False)
    observacao = forms.CharField(label=_("Observation"), max_length=1024, required=False)
    
    def clean(self):
        raise forms.ValidationError('Teste')