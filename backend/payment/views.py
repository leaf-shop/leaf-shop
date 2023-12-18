from rest_framework import viewsets, response, status
from orders import serializers as orders_serializers
from orders import models as orders_models
from . import models, serializers



class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class PaymentViewSet(viewsets.ViewSet):
    def get_last_order(self, user_id):
        return orders_models.Order.objects.filter(
            user_id=user_id,
            status=orders_models.Order.STATUS_OPTIONS[2][0]).last()
        

    def calculate_price(self, request, user_id):
        order = self.get_last_order(user_id)

        if not order:
            return response.Response("Open order is not found", status=status.HTTP_404_NOT_FOUND)
        
        serialized_order = orders_serializers.OrderOutputSerializer(order)

        price = order.calculate_price()

        return response.Response(
            {
                "total_price": price,
                "order": serialized_order.data
            },
            status=status.HTTP_200_OK)
    

    def pay(self, request, user_id):
        pass

        # order = self.get_last_order(user_id)

        # if not order:
        #     return response.Response("Order not found", status=status.HTTP_404_NOT_FOUND)

        # price = order.calculate_price()

        # send data and request to payment interface to declare the purchase 
        #  price , token , etc
        # recieve the data from request resopnse
        

        # redirect user to interface with propriate data
        # return 
    

    def succeed_purchase(self, request):
        pass


        
    