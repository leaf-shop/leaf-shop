from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()


route.register("admin", views.CustomUserForAdminViewSet)
route.register("user", views.CustomUserViewSet)
urlpatterns = route.urls
