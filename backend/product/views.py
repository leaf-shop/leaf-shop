from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets, status
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers


@method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAdminUser]


    def apply_discount_category(self, request, category_id, discount_id):
        models.Product.objects.filter(
            category__in=[category_id]).all().update(discount=discount_id)
        return Response(status=status.HTTP_200_OK)


    def remove_discount_category(self, request, category_id):
        products_to_update = models.Product.objects.filter(
            category__in=[category_id]).all()

        for product in products_to_update:
            product.discount = None
            product.save()

        return Response(status=status.HTTP_200_OK)


    def apply_discount_group(self, request, discount_id, products_list):

        try:
            products_list = [int(x) for x in products_list.split(",")]
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        for pk in products_list:
            models.Product.objects.filter(
                id=pk).all().update(discount=discount_id)

        return Response(status=status.HTTP_200_OK)


    def remove_discount_group(self, request, products_list):

        try:
            products_list = [int(x) for x in products_list.split(",")]
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

        products_to_update = models.Product.objects.filter(
            id__in=products_list).all()

        for product in products_to_update:
            product.discount = None
            product.save()

        return Response(status=status.HTTP_200_OK)


class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGallery.objects.all()
    serializer_class = serializers.ProductGallerySerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]

    @action(detail=False, methods=["get"])
    def default(self, request, **kwargs):
        query = self.queryset.filter(is_default=True)
        serialized_data = self.serializer_class(query, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
