from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


route = DefaultRouter()
route.register("tickets/ticket", views.TicketViewSet)
route.register("tickets/comments", views.CommentViewSet)

urlpatterns = [
    path("tickets/ticket/tickets_by_assignee/<int:assignee_id>/", views.TicketViewSet.as_view({"get": "tickets_by_assignee"})),
    path("tickets/ticket/tickets_by_creator/<int:creator_id>/", views.TicketViewSet.as_view({"get": "tickets_by_creator"})),
    path("tickets/comments/comments_by_creator/<int:creator_id>/", views.CommentViewSet.as_view({"get": "comments_by_creator"})),
]+route.urls
