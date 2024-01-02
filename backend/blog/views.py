from shared.permissions import IsAdminUserOrReadOnly
from . import models, serializers
from rest_framework import viewsets, response, status



class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_number_of_blogs_by_created_time(self, request, number):

        if number < 1 :
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        
        blogs = self.queryset.order_by("-created_datetime").all()[:number]

        serialized_data = self.get_serializer_class()(blogs, many=True)
        
        return response.Response(serialized_data.data, status=status.HTTP_200_OK)
