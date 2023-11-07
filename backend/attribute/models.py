from django.db import models


class Attribute(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False, blank=True)
