from django.urls import path

from .views import index, brand_create, ListCreateBrandAPIView

urlpatterns = [
    path('', index, name='index'),
    path('brand_create', brand_create, name='brand-create'),
    path('brands', ListCreateBrandAPIView.as_view(), name='brand-list-create'),
]
