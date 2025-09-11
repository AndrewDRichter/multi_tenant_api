from rest_framework.serializers import ModelSerializer
from .models import Entity
from django.contrib.auth.models import User


class EntitySerializer(ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
