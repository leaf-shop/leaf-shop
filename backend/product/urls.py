from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()

route.register("product", views.ProductViewSet)
route.register("productgallery", views.ProductGalleryViewSet)

urlpatterns = route.urls
