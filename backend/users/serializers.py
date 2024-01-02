from rest_framework import serializers
from . import models


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = "__all__"

class CustomUserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ["email", "username", "first_name", "last_name", "phone_number", "password", "favorites"]

class CustomUserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ["username", "email", "first_name", "last_name", "phone_number", "favorites"]
