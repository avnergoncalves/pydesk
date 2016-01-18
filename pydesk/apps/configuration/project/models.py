# coding: utf-8

from django.db import models
from pydesk.apps.configuration.project.managers import GridProjectManager


class Project(models.Model):

    description = models.CharField(max_length=200, blank=False)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    grid = GridProjectManager()

    class Meta:
        db_table = 'project'