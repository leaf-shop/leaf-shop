from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets
from . import models, serializers


class DiscountViewSet(viewsets.ModelViewSet):
    
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]
