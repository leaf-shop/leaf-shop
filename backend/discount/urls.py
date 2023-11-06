from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("discount", views.DiscountViewset)

urlpatterns = route.urls