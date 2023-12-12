from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . import models, serializers


@method_decorator(csrf_exempt, name='dispatch')
class CustomUserForAdminViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserAdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    

@method_decorator(csrf_exempt, name='dispatch')
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return serializers.CustomUserOutputSerializer if self.request.method == "GET" else serializers.CustomUserInputSerializer
    
    def  get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        else:
            return self.permission_classes
    