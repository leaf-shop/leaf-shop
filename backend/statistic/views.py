from datetime import timezone
from datetime import datetime
from rest_framework import generics, response, status
from django.contrib.auth import get_user_model
from statistic import models
from support import models as support_models
from django.utils.timezone import make_aware
from online_users.models import OnlineUserActivity
from datetime import timedelta
from . import serializers


class RegistrationStatisticAPIView(generics.GenericAPIView):

    def get(self, request, start_time=None, end_time=None, *args, **kwargs):

        if end_time is None:
            end_time = timezone.now().replace(hour=23, minute=59, second=59, microsecond=0)

        try:
            end_time = make_aware(datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ'))
        except ValueError:
            return response.Response({'error': 'Invalid end_time format'}, status=status.HTTP_400_BAD_REQUEST)
        
        if start_time is None:
            start_time = timezone.now()
        
        try:
            start_time = make_aware(datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ'))
        except ValueError:
            return response.Response({'error': 'Invalid start_time format'}, status=status.HTTP_400_BAD_REQUEST)

        registrations = get_user_model().objects.filter(date_joined__range=(start_time, end_time)).all()
        registrations_count = registrations.count()

        serialized_data = serializers.RegistrationStaticsSerializers({
                "count": registrations_count,
                "users": registrations
            })

        return response.Response(
            serialized_data.data,
            status=status.HTTP_200_OK
            )


class TicketStatisticAPIView(generics.GenericAPIView):

    def get(self, request, start_time=None, end_time=None, *args, **kwargs):

        if end_time is None:
            end_time = timezone.now().replace(hour=23, minute=59, second=59, microsecond=0)

        try:
            end_time = make_aware(datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ'))
        except ValueError:
            return response.Response({'error': 'Invalid end_time format'}, status=status.HTTP_400_BAD_REQUEST)
        
        if start_time is None:
            start_time = timezone.now()
        
        try:
            start_time = make_aware(datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ'))
        except ValueError:
            return response.Response({'error': 'Invalid start_time format'}, status=status.HTTP_400_BAD_REQUEST)

        tickets = support_models.Ticket.objects.filter(created_at__range=(start_time, end_time)).all()
        tickets_count = tickets.count()

        serialized_data = serializers.TicketsStaticsSerializer(
            {
            "count": tickets_count,
            "tickets": tickets
            })

        return response.Response(
            serialized_data.data, 
            status=status.HTTP_200_OK
            )

class RequestStatisticsAPIView(generics.GenericAPIView):
    queryset = models.DailyRequestCount.objects.all()
    serializer_class = serializers.RequestStatisticsSerializer
    def get(self, request):
        requests = self.queryset.order_by("-date")
        serialized_data = self.serializer_class(requests, many=True)
        return response.Response(serialized_data.data, status=status.HTTP_200_OK)


class OnlineUserAPIView(generics.GenericAPIView):
    def get(self, request):
        online_users_count = OnlineUserActivity.get_user_activities(time_delta=timedelta(minutes=2)).count()
        return response.Response(
            {
                "count": online_users_count,
            }, 
            status=status.HTTP_200_OK)
