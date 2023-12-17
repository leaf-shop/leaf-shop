from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("product", views.ProductViewSet)
route.register("productgallery", views.ProductGalleryViewSet)
route.register("attribute", views.AttributeViewSet)

urlpatterns = route.urls



