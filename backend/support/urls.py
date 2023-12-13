from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


route = DefaultRouter()
route.register("tickets/ticket", views.TicketViewSet)
route.register("tickets/comments", views.CommentViewSet)

urlpatterns = route.urls
