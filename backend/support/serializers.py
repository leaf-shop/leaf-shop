from rest_framework import serializers
from . import models as support_model



class TicketCommentOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = support_model.TicketComment
        fields = [
            "id",
            "ticket",
            "text",
            "created_at",
            "author"
        ]


class TicketCommentInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = support_model.TicketComment
        fields = [
            "ticket",
            "text",
            "author"
        ]


class TicketOutputSerializer(serializers.ModelSerializer):
    comments = TicketCommentOutputSerializer(many=True)
    class Meta:
        model = support_model.Ticket
        fields = [
            'id', 'title', 'description', 'created_at',
            'creator', 'assignee', 'status', 'comments'
        ]


class TicketInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = support_model.Ticket
        fields = [
            'id', 'title', 'description', 'created_at',
            'creator', 'assignee', 'status', 'comments'
        ]
