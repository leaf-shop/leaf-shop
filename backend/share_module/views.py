from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer