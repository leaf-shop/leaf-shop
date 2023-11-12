from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
