"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/discount/", include('discount.urls')),
    path("api/product/", include('product.urls')),
    path("api/support/", include('support.urls')),
    path("api/shared/", include('shared.urls')),
    path("api/blog/", include('blog.urls')),
    path('api/accounts/auth/', include('djoser.urls.authtoken')),
    path("api/accounts/", include('users.urls')),
    path("api/orders/", include('orders.urls')),
    path('swagger/', swagger.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
