# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=datetime.now, blank=True)
    input = models.CharField(max_length=50)
    result = models.TextField()

class Setting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
