from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from django.db.models import Q
from . import serializers
from . import models


class OrderViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'get', 'put', 'patch']
    queryset = models.Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.OrderOutputSerializer
        return serializers.OrderInputSerializer

    @action(detail=False, methods=['get'])
    def get_last_order(self, request, *args, **kwargs):

        user_id = self.request.user.id
        if user_id is None:
            return response.Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = self.queryset.filter(
            user_id=user_id).order_by('-datetime_created').first()
        if queryset is None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        serialized_data = self.get_serializer_class()(queryset).data
        return response.Response(data=serialized_data, status=status.HTTP_200_OK)


class OrderItemViewSet(viewsets.ModelViewSet):
    OUTPUT_SERIALIZER_CLASS = serializers.OrderItemOutputSerializer
    INPUT_SERIALIZER_CLASS = serializers.OrderItemInputSerializer
    queryset = models.OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.OUTPUT_SERIALIZER_CLASS
        return self.INPUT_SERIALIZER_CLASS

    @action(detail=False, methods=['post'])
    def add_to_order(self, request, *args, **kwargs):

        user = self.request.user
        last_order, _ = models.Order.objects.get_or_create(
            user_id=user.id,
            status='u'
        )

        serialized_request = self.get_serializer_class()(data=request.data)
        if serialized_request.is_valid():
            validated_data = serialized_request.validated_data
        else:
            return response.Response({"detail": "enter valid paramter"}, status=status.HTTP_400_BAD_REQUEST)

        product_id = validated_data["product"]
        quantity = validated_data["quantity"]

        try:
            order_item = models.OrderItem.objects.filter(
                Q(order_id=last_order.id) & Q(product_id=product_id)).first()
        except:
            return response.Response({"detail": "enter valid paramter"}, status=status.HTTP_400_BAD_REQUEST)

        if order_item:

            order_item.quantity += quantity
            order_item.save()

            return response.Response(
                self.OUTPUT_SERIALIZER_CLASS(order_item).data, status=status.HTTP_200_OK)

        validated_data["order"] = last_order
        order_item = models.OrderItem.objects.create(**validated_data)
        order_item.save()

        return response.Response(self.OUTPUT_SERIALIZER_CLASS(order_item).data, status=status.HTTP_201_CREATED)
