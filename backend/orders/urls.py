from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("order", views.OrderViewSet, basename="order")
route.register("items", views.OrderItemViewSet, basename="items")
urlpatterns = [
    path("order/get-last-order/<int:user_id>/", views.OrderViewSet.as_view({"get": "get_last_order"})),
    path("order/get-user-all-orders/<int:user_id>/", views.OrderViewSet.as_view({"get": "get_user_all_orders"})),
    path("items/add-to-order/<int:user_id>/", views.OrderItemViewSet.as_view({"post": "add_to_order"})),
    path("order/filter/<str:state>/<int:number>/", views.OrderViewSet.as_view({"get": "get_orders_by_number_status"})),
]+route.urls
