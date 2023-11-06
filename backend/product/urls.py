from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("Product", views.ProductViewSet)

urlpatterns = [] + route.urls