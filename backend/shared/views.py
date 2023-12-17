from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, generics, status
from blog.models import Blog
from product import serializers as productSerializers
from blog import serializers as blogSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from product.models import Product
from . import models, serializers
from django.db.models import Q


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]


class SearchAPIView(generics.RetrieveAPIView):
    """
    it returns a list of matching product or comment based on query
    input querystrings :
    -sort  {0,1} => default is 0 for descending and 1 for ascending
    -model {'product', 'blog'}. This field is required 
    -search_for  this is word for searching
    -attribute  which is list IDs of required attributes

    example query: 
    http://127.0.0.1:8000/api/shared/search/blog/?search_for=somthing&sotr=1
    or 
    http://127.0.0.1:8000/api/shared/search/product/?search_for=somthing&sotr=1
    or 
    http://127.0.0.1:8000/api/shared/search/product/?attribute=1,2,3,,4

    """
    pagination_class = PageNumberPagination

    class SortFilterValues(enumerate):
        ORDER_BY_DESCENDING = '-created_datetime'
        ORDER_BY_ASCENDING = 'created_datetime'

    class SortQueryStringValues(enumerate):
        DESCENDING = 0
        ASCENDING = 1

    class QueryModels(enumerate):
        BLOG_MODEL = "blog"
        PRODUCT_MODEL = "product"

    def get_serializer_class(self, model):
        if model == self.QueryModels.PRODUCT_MODEL:
            return productSerializers.ProductSerializer
        elif model == self.QueryModels.BLOG_MODEL:
            return blogSerializer.BlogSerializer
        else:
            return super().get_serializer_class()

    def get(self, request, search_model, *args, **kwargs):
        sort = request.GET.get("sort", self.SortQueryStringValues.DESCENDING)
        search_for = request.GET.get("search_for")
        attributes = request.GET.get("attribute")
        attribute_query = Q()
        search_for_query = Q()
        model = None

        if search_model == self.QueryModels.PRODUCT_MODEL:
            model = Product
        elif search_model == self.QueryModels.BLOG_MODEL:
            model = Blog
        else:
            return Response("Bad Request: enter 'model' for search ", status=status.HTTP_400_BAD_REQUEST)

        if sort == self.SortQueryStringValues.DESCENDING:
            sorted_by = self.SortFilterValues.ORDER_BY_DESCENDING

        else:
            sorted_by = self.SortFilterValues.ORDER_BY_ASCENDING

        try:
            if attributes:
                attributes = [int(x) for x in attributes.split(",")]
                for id in attributes:
                    attribute_query |= Q(attribute__id=id)

            if search_for:
                search_for_query |= Q(title__icontains=search_for) | Q(
                    description__icontains=search_for)

            general_query = model.objects.filter(
                search_for_query | attribute_query).order_by(sorted_by).all()

        except:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

        page = self.paginate_queryset(general_query)
        serialized_data = self.get_serializer_class(
            search_model)(page, many=True)
        return self.get_paginated_response(serialized_data.data)
