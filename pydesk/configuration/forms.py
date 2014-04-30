'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, IntegerField, EmailField, CharField, BooleanField
from pydesk.configuration.models import Enterprise, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField
from django.forms.forms import Form

##CUSTON FIELDS
class EnterpriseModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.rasao_social

##FORMS
class EnterpriseForm(ModelForm):
    id = IntegerField(widget=HiddenInput(), required=False)
    
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


class UserForm(UserCreationForm):
    first_name = CharField(required=True, widget=TextInput(attrs={'size': 50}), label=_('First Name'))
    last_name = CharField(required=True, widget=TextInput(attrs={'size': 50}), label=_('Last Name'))
    email = EmailField(required=True, widget=TextInput(attrs={'size': 40}), label=_('E-mail'))

    enterprise = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Enterprise'))
    phone = CharField(required=False, widget=TextInput(attrs={'size': 20}), label=_('Phone'))
    celphone = CharField(required=False, widget=TextInput(attrs={'size': 20}), label=_('Celphone'))
    receive_email = BooleanField(label=_('Receive E-mail'))

    class Meta:
        model = User
        fields = ( "username", "first_name", "last_name", "email", "enterprise", "phone", "celphone", "receive_email")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        try:
            user_profile = user.get_profile()
        except ObjectDoesNotExist:
            user_profile = UserProfile()

        user_profile.enterprise = self.cleaned_data['enterprise']
        user_profile.phone = self.cleaned_data['phone']
        user_profile.cell_phone = self.cleaned_data['celphone']
        user_profile.receive_email = self.cleaned_data['receive_email']

        if commit:
            user.save()

            user_profile.user = user
            user_profile.save()

        return user


class UserRelationshipsForm(Form):

    equipe = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Equipe'))
    perfil = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Perfil'))
    permissao = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Permissao'))
    tipo_ic = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Tipo Ic'))

    def save(self, user, commit=True):
        user_profile = user.get_profile()


        if commit:
            user_profile.save()

        return user