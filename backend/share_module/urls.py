from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("Category", views.CategoryViewSet)
route.register("Comment", views.CommentViewSet)

urlpatterns = route.urls

