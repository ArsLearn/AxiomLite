from django.db import models as m
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = {
        "owner": "Owner",
        "admin": "Admin",
        "user": "User",
        "member": "Member",
        "vip": "VIP",
        "sponsor": "Sponsor",
    }
    phone_number = m.CharField(max_length = 11)
    national_code = m.CharField(max_length = 10)
    born_date = m.DateField(null = True)
    level = m.PositiveIntegerField(max_length = 4, default = 1)
    