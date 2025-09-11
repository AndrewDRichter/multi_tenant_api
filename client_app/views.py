from django.http import HttpResponse
from .models import Entity
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.decorators import login_required
from .serializers import EntitySerializer, UserSerializer


class ListCreateEntityAPIView(ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class ListCreateUserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@login_required
def index(request):
    user = request.user
    return HttpResponse(f'<h1>Homepage {user}</h1>')
