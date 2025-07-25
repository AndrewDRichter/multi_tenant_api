from django.shortcuts import render, redirect
from .models import Brands
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from .serializers import BrandSerializer


class ListCreateBrandAPIView(ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer

def index(request):
    brands = Brands.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'index.html', context)

def brand_create(request):
    if request.POST:
        name = request.POST.get('name')
        brand = Brands(name=name)
        brand.save()
        return redirect('index')
