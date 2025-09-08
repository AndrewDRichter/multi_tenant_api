from django.http import HttpResponse
from .models import Brands
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.decorators import login_required
from .serializers import BrandSerializer


class ListCreateBrandAPIView(ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer

@login_required
def index(request):
    user = request.user
    return HttpResponse(f'<h1>Homepage {user}</h1>')
