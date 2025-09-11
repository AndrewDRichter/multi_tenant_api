from django.db import models
from django.contrib.auth.models import User


class ClientUser(User):
    is_tenant_admin = models.BooleanField(default=False)
