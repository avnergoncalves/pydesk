# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from pydesk.apps.configuration.enterprise.models import Enterprise
from pydesk.apps.configuration.user.managers import GridUserManager


class Equipe(models.Model):
    description = models.CharField(max_length=200, blank=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    enterprise = models.ForeignKey(Enterprise)
    esquipes = models.ManyToManyField(Equipe)
    receive_email = models.BooleanField(blank=False, default=True)
    color_system = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    cell_phone = models.CharField(max_length=200, blank=False)
    auto_update_dashboard = models.BooleanField(blank=False, default=False)

    objects = models.Manager()
    grid = GridUserManager()