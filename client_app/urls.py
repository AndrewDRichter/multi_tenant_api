from django.urls import path

from .views import index, brand_create

urlpatterns = [
    path('', index, name='index'),
    path('brand_create', brand_create, name='brand-create'),
]
