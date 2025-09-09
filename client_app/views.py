from django.http import HttpResponse
from .models import Brands
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.decorators import login_required
from .serializers import BrandSerializer, UserSerializer


class ListCreateBrandAPIView(ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer


class ListCreateUserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@login_required
def index(request):
    user = request.user
    return HttpResponse(f'<h1>Homepage {user}</h1>')
