from rest_framework import viewsets
from . import models, serializers



class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGallery.objects.all()
    serializer_class = serializers.ProductGallerySerializer
