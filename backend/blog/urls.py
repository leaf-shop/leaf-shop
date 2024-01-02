from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("blog", views.BlogViewSet)

urlpatterns = [
    path("blog/blogs-number-by-created-time/<int:number>/",
         views.BlogViewSet.as_view({"get": "get_number_of_blogs_by_created_time"}))
] + route.urls