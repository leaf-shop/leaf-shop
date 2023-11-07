from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("", views.AttributeViewSet)

urlpatterns = [
    path("default/", views.DefaultAttributeViewSet.as_view()),
] + route.urls
