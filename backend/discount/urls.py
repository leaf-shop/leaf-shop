from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("discount", views.DiscountViewSet)

urlpatterns = route.urls