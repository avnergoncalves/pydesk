# coding: utf-8

from django.db import models
from pydesk.apps.configuration.equip.managers import GridEquipManager


class Equip(models.Model):

    description = models.CharField(max_length=200, blank=False)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    grid = GridEquipManager()

    class Meta:
        db_table = 'equip'