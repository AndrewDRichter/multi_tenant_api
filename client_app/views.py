from django.http import HttpResponse
from .models import Brands
from rest_framework.generics import ListCreateAPIView
from .serializers import BrandSerializer


class ListCreateBrandAPIView(ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer


def index(request):
    print(request.user)
    return HttpResponse('<h1>Homepage</h1>')
