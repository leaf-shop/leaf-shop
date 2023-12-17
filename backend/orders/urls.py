from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("order", views.OrderViewSet, basename="order")
route.register("items", views.OrderItemViewSet, basename="items")
urlpatterns = [
    path("order/get_last_order/<int:user_id>/", views.OrderViewSet.as_view({"get": "get_last_order"})),
    path("order/get_user_all_orders/<int:user_id>/", views.OrderViewSet.as_view({"get": "get_user_all_orders"})),
    path("items/add_to_order/<int:user_id>/", views.OrderItemViewSet.as_view({"post": "add_to_order"})),
]+route.urls
