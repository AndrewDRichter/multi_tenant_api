from django.urls import path

from .views import index, brand_create

urlpatterns = [
    path('', index, name='client_index'),
    path('brand_create/<str:name>', brand_create, name='brand-create'),
]
