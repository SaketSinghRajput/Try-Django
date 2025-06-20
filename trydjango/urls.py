"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from pages.views import homepage_view, contact_view, about_view
from products.views import (
    product_detail_view, 
    product_create_view,
    
    dynamic_lookup_view
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path('', homepage_view, name='home'),
    path('create/', product_create_view),
    path('contact/', contact_view),
    path('products/<int:my_id>',dynamic_lookup_view, name='product'),
    path('about/', about_view),
]

