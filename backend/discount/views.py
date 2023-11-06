from rest_framework import viewsets
from . import models, serializers


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
