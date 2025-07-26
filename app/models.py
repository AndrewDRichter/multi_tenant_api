from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User


class Client(TenantMixin):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)


class Domain(DomainMixin):
    pass


class TenantUser(User):
    tenant = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='users')
