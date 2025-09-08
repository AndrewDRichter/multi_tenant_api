# from django.urls import path

# from .views import ListCreateBrandAPIView, index

# urlpatterns = [
#     path('', index, name='index'),
#     path('brands', ListCreateBrandAPIView.as_view(), name='brand-list-create'),
# ]
# from .views import index, login_view
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('login', login_view, name='login'),
]
