from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("address", views.AddressViewSet)


urlpatterns = [
    path("calculate_price/<int:user_id>/", views.PaymentViewSet.as_view({"get":"calculate_price"}), name="calculate_price"),
    path("pay/<int:user_id>/", views.PaymentViewSet.as_view({"get": "pay"}), name="pay"),
]
