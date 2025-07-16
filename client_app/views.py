from django.shortcuts import render
from .models import Brands
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome to the tenant page</h1>')

def brand_create(request, name):
    brand = Brands(name=name)
    brand.save()
    return HttpResponse(f'<h1>Brand: {brand.name} created.</h1>')
