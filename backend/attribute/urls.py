from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("attribute", views.AttributeViewSet)

urlpatterns = route.urls
