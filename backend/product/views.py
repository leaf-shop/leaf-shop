from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from . import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGallery.objects.all()
    serializer_class = serializers.ProductGallerySerializer




class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer


class DefaultAttributeViewSet(generics.RetrieveAPIView):
    serializer_class = serializers.AttributeSerializer

    def get(self, request, **kwargs):
        query = models.Attribute.objects.filter(is_default=True)
        serialized_data = self.serializer_class(query, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
