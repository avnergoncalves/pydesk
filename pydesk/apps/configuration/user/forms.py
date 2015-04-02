# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput, EmailField, CharField, BooleanField
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField
from django.forms.forms import Form
from django.contrib.auth.models import User

from pydesk.apps.configuration.user.models import UserProfile
from pydesk.apps.configuration.enterprise.models import Enterprise

##CUSTON FIELDS
class EnterpriseModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.rasao_social


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
        fields = ("username", "first_name", "last_name", "email", "enterprise", "phone", "celphone", "password1",
                  "password2", "receive_email")

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