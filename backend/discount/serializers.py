from rest_framework import serializers
from . import models

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discount
        fields = "__all__"