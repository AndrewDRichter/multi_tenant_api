from django.shortcuts import render, redirect
from .models import Brands
from django.http import HttpResponse


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
