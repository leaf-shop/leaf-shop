from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from . import models, serializers


class DiscountViewSet(viewsets.ModelViewSet):
    
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
    permission_classes = [IsAdminUser]
