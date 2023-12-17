from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets, generics, status
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers


@method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]


class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGallery.objects.all()
    serializer_class = serializers.ProductGallerySerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]


@method_decorator(csrf_exempt, name='dispatch')
class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]

    @action(detail=False, methods=["get"])
    def default(self, request, **kwargs):
        query =self.queryset.filter(is_default=True)
        serialized_data = self.serializer_class(query, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
