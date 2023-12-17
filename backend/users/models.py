from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    favorites = models.ManyToManyField("product.Product", blank=True)
