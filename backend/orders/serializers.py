from rest_framework import serializers
from product import serializers as product_serializer
from . import models



class OrderItemOutputSerializer(serializers.ModelSerializer):
    product = product_serializer.ProductSerializer()

    class Meta:
        model = models.OrderItem
        fields = '__all__'


class OrderItemInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['order', 'product', 'quantity']


class OrderOutputSerializer(serializers.ModelSerializer):
    items = OrderItemOutputSerializer(many=True)

    class Meta:
        model = models.Order
        fields = '__all__'


class OrderInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['user', 'status',]