# coding: utf-8
from django.forms.widgets import HiddenInput, PasswordInput

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import TextInput, EmailField, CharField, BooleanField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField

from django.contrib.auth.models import User

from pydesk.apps.configuration.user.models import UserProfile
from pydesk.apps.configuration.enterprise.models import Enterprise

##CUSTON FIELDS
class EnterpriseModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.rasao_social


class CustomUserCreationForm(UserCreationForm):

    first_name = CharField(required=True, widget=TextInput(attrs={'size': 50}), label=_('First Name'))
    last_name = CharField(required=True, widget=TextInput(attrs={'size': 50}), label=_('Last Name'))
    email = EmailField(required=True, widget=TextInput(attrs={'size': 40}), label=_('E-mail'))

    enterprise = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Enterprise'))
    phone = CharField(required=False, widget=TextInput(attrs={'size': 20}), label=_('Phone'))
    celphone = CharField(required=False, widget=TextInput(attrs={'size': 20}), label=_('Celphone'))
    receive_email = BooleanField(label=_('Receive E-mail'))

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "enterprise", "phone", "celphone", "password1",
                  "password2", "receive_email")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)

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


class CustomUserChangeForm(UserChangeForm):

    id = CharField(required=True, widget=HiddenInput(attrs={'size': 50}), label=_('First Name'))
    first_name = CharField(required=True, widget=TextInput(attrs={'size': 50}), label=_('First Name'))
    last_name = CharField(required=True, widget=TextInput(attrs={'size': 50}), label=_('Last Name'))
    email = EmailField(required=True, widget=TextInput(attrs={'size': 40}), label=_('E-mail'))
    password = CharField(required=False, widget=PasswordInput(attrs={'size': 50}), label=_('Password'))
    password_confirm = CharField(required=False, widget=PasswordInput(attrs={'size': 50}), label=_('Password confirmation'))

    enterprise = EnterpriseModelChoiceField(queryset=Enterprise.objects.all(), label=_('Enterprise'))
    phone = CharField(required=False, widget=TextInput(attrs={'size': 20}), label=_('Phone'))
    celphone = CharField(required=False, widget=TextInput(attrs={'size': 20}), label=_('Celphone'))
    receive_email = BooleanField(required=False, label=_('Receive E-mail'))

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "enterprise", "phone", "celphone", "password",
                  "password_confirm", "receive_email")

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            try:
                user_profile = kwargs['instance'].get_profile()
            except ObjectDoesNotExist:
                user_profile = UserProfile()

            kwargs.setdefault('initial', {})['enterprise'] = user_profile.enterprise.id
            kwargs.setdefault('initial', {})['phone'] = user_profile.phone
            kwargs.setdefault('initial', {})['celphone'] = user_profile.cell_phone
            kwargs.setdefault('initial', {})['receive_email'] = user_profile.receive_email

        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    def clean_password_confirm(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password_confirm")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(CustomUserChangeForm, self).save(commit=False)

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