from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductGallery
        fields = '__all__'