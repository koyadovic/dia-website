from django.contrib.postgres.fields import JSONField
from django.db import models


class ServerConfiguration(models.Model):
    key = models.CharField(unique=True, blank=False, null=False, default='', max_length=255)
    value = JSONField(blank=True, null=False, default={})
