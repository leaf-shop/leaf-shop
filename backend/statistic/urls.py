from django.urls import path
from . import views

urlpatterns = [
    path("registration/<str:start_time>/<str:end_time>/", views.RegistrationStatisticAPIView.as_view()),
    path("tickets/<str:start_time>/<str:end_time>/", views.TicketStatisticAPIView.as_view()),
    path("requests/", views.RequestStatisticsAPIView.as_view()),
]
