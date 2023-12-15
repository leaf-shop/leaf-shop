from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from . import models, serializers

# TODO: decorators should be removed for production

@method_decorator(csrf_exempt, name='dispatch')
class TicketViewSet(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.TicketOutputSerializer
        return serializers.TicketInputSerializer

    @action(detail=False, methods=['get'])
    def tickets_by_assignee(self, request):
        assignee_id = self.request.GET.get("id")
        if not assignee_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.filter(assignee_id=assignee_id)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def tickets_by_creator(self, request):
        creator_id = self.request.GET.get("id")
        if not creator_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.filter(creator_id=creator_id)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.TicketComment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.TicketCommentOutputSerializer
        return serializers.TicketCommentInputSerializer

    @action(detail=False, methods=['get'])
    def comments_by_creator(self, request):
        creator_id = self.request.GET.get("id")
        if not creator_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.filter(author_id=creator_id)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
