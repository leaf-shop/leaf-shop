from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from . import models, serializers
from django.db.models import Q


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGallery.objects.all()
    serializer_class = serializers.ProductGallerySerializer




class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer


class DefaultAttributeAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.AttributeSerializer

    def get(self, request, **kwargs):
        query = models.Attribute.objects.filter(is_default=True)
        serialized_data = self.serializer_class(query, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class SearchAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductSerializer

    def get(self, request, *args, **kwargs):

        search_for = request.GET.get("search_for")
        attributes = request.GET.get("attribute")
        attribute_query = Q()
        search_for_query = Q()

        try:
            if attributes:
                attributes = [int(x) for x in attributes.split(",")]
                for id in attributes:
                    attribute_query |= Q(attribute__id=id)

            if search_for:
                search_for_query |= Q(title__icontains=search_for) | Q(
                    description__icontains=search_for)

            product_query = models.Product.objects.filter(
                search_for_query | attribute_query).all()

        except:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

        serialized_data = self.serializer_class(product_query, many=True)

        if serialized_data.data == []:
            return Response("Not Fount", status=status.HTTP_404_NOT_FOUND)

        return Response(serialized_data.data)
