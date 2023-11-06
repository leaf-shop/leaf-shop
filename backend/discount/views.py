from rest_framework import viewsets
from . import models, serializers


class DiscountViewset(viewsets.ModelViewSet):
    serializre_class = serializers.DiscountSerializer
    queryset = models.Discount.objects.all()
