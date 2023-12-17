from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("category", views.CategoryViewSet)
route.register("comment", views.CommentViewSet)

urlpatterns = [
    path("search/<str:search_model>/", views.SearchAPIView.as_view()),
    path("comment/<int:user_id>/", views.CommentViewSet.as_view({"get": "get_by_user_id"}))
] + route.urls