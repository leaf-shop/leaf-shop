from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

route = DefaultRouter()

route.register("blog", views.BlogViewSet)

urlpatterns = route.urls