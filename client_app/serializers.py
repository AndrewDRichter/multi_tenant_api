from rest_framework.serializers import ModelSerializer
from .models import Brands


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brands
        fields = '__all__'
