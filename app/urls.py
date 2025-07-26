from .views import index, login_view
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login', login_view, name='login'),
]
