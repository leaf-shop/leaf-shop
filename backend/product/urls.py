from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("product", views.ProductViewSet)
route.register("productgallery", views.ProductGalleryViewSet)
route.register("attribute", views.AttributeViewSet)

urlpatterns = [
    path("admin/discount/category/add/<int:category_id>/<int:discount_id>/",
         views.ProductViewSet.as_view({"get": "apply_discount_category", })),
    path("admin/discount/category/remove/<int:category_id>/",
         views.ProductViewSet.as_view({"get": "remove_discount_category"})),
    path("admin/discount/add/<int:discount_id>/<str:products_list>/",
         views.ProductViewSet.as_view({"get": "apply_discount_group"})),
    path("admin/discount/remove/<str:products_list>/",
         views.ProductViewSet.as_view({"get": "remove_discount_group"})),
] + route.urls
