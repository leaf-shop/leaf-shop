from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import viewsets
from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]

    # def get_permissions(self):
    #     return [AllowAny()] if self.request.method == "GET" else [IsAdminUser()]
         

