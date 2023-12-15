from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("order", views.OrderViewSet, basename="order")
route.register("items", views.OrderItemViewSet, basename="items")
urlpatterns = route.urls