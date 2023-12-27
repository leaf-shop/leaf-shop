from shared.permissions import IsAdminUserOrReadOnly
from . import models, serializers
from rest_framework import viewsets



class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]