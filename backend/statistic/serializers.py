from rest_framework import serializers
from statistic import models
from users import serializers as user_serializers
from support import serializers as support_serializers


class RegistrationStaticsSerializers(serializers.Serializer):
    count = serializers.IntegerField()
    users = user_serializers.CustomUserOutputSerializer(many=True, read_only=True)


class TicketsStaticsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    tickets = support_serializers.TicketOutputSerializer(many=True)


class RequestStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyRequestCount
        fields = "__all__"