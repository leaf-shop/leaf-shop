from django.shortcuts import render
from . import models, serializers
# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer