from django.urls import path

from .views import ListCreateBrandAPIView, index

urlpatterns = [
    path('', index, name='index'),
    path('brands', ListCreateBrandAPIView.as_view(), name='brand-list-create'),
]
