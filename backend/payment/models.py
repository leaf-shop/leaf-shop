from django.db import models
from users.models import CustomUser






class Address(models.Model):
    user = models.ForeignKey(CustomUser, related_name="addresses", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
