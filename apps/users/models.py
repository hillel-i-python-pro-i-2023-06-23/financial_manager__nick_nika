from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="custom_users")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_users")
