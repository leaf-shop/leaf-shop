from django.db import models
from users.models import CustomUser






class Address(models.Model):
    user = models.OneToOneField(CustomUser, related_name="addresses", on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)