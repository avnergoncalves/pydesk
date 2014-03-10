'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, IntegerField, EmailField, CharField
from configuration.models import Enterprise, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField

##CUSTON FIELDS
class EnterpriseModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.rasao_social

##FORMS
class EnterpriseForm(ModelForm):
    id = IntegerField(widget=HiddenInput, required=False)
    
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


class UserCreateForm(UserCreationForm):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField(required=True)

    enterprise = EnterpriseModelChoiceField(queryset=Enterprise.objects.all())

    class Meta:
        model = User
        fields = ( "username", "first_name", "last_name", "email", "enterprise" )


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        try:
            user_profile = user.get_profile()
        except ObjectDoesNotExist:
            user_profile = UserProfile(user=user)

        user_profile.enterprise_id = self.cleaned_data['enterprise']
        #user_profile.url = self.cleaned_data['url']

        if commit:
            user.save()
            user_profile.save()
        return user