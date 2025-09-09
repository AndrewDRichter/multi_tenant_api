from rest_framework.serializers import ModelSerializer
from .models import Brands
from django.contrib.auth.models import User


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brands
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
