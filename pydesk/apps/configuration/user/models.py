# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from pydesk.apps.configuration.enterprise.models import Enterprise
from pydesk.apps.configuration.equip.models import Equip
from pydesk.apps.configuration.project.models import Project
from pydesk.apps.configuration.user.managers import GridUserManager


class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='user')
    receive_email = models.BooleanField(blank=False, default=True)
    color_system = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    cell_phone = models.CharField(max_length=200, blank=False)
    auto_update_dashboard = models.BooleanField(blank=False, default=False)
    enterprise = models.ManyToManyField(Enterprise)
    equip = models.ManyToManyField(Equip)
    project = models.ManyToManyField(Project)

    objects = models.Manager()
    grid = GridUserManager()

    class Meta:
        db_table = 'userprofile'