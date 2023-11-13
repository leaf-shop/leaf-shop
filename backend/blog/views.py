from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer