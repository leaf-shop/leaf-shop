from rest_framework.permissions import AllowAny, IsAdminUser
from product import serializers as productSerializers
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers
from product.models import Product
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
    class QueryStringValue(enumerate):
        OrderByDescending = '-created_datetime'
        OrderByAscending = 'created_datetime'
        BlogModel = "blog"
        ProductModel = "product"

    # product_serializer_class = productSerializers.ProductSerializer
    def get_serializer_class(self, model):
        if model == self.QueryStringValue.ProductModel:
            return productSerializers.ProductSerializer
        elif model == self.QueryStringValue.BlogModel:
            return blogSerializer.BlogSerializer
        else:
            return super().get_serializer_class()
            
                




    def get(self, request, test=QueryStringValue.OrderByDescending, *args, **kwargs):

        search_for = request.GET.get("search_for")
        attributes = request.GET.get("attribute")
        search_model = request.GET.get("model")
        attribute_query = Q()
        search_for_query = Q()
        model = None

        if search_model is None:
            return Response("Bad Request: enter 'model' for search ", status=status.HTTP_400_BAD_REQUEST)

        elif search_model == self.QueryStringValue.ProductModel:
            model = Product
        else:
            #  model = Blog
            pass

        try:
            if attributes:
                attributes = [int(x) for x in attributes.split(",")]
                for id in attributes:
                    attribute_query |= Q(attribute__id=id)

            if search_for:
                search_for_query |= Q(title__icontains=search_for) | Q(
                    description__icontains=search_for)

            general_query = model.objects.filter(
                search_for_query | attribute_query
                ).order_by('-created_datetime').all()

        except:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

        serialized_data = self.get_serializer_class(search_model)(general_query, many=True)

        if serialized_data.data == []:
            return Response("Not Fount", status=status.HTTP_404_NOT_FOUND)

        return Response(serialized_data.data)
