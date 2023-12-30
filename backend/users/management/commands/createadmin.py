from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser if one does not exist'

    def handle(self, *args, **options):
        username = settings.SUPERUSER_USERNAME
        password = settings.SUPERUSER_PASSWORD


        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username, 
                password=make_password(password))
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully"))
        else:
            self.stdout.write(self.style.SUCCESS(f"User with username '{username}' already exists"))