from django.db import models as m
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = m.CharField(max_length = 11)
    national_code = m.CharField(max_length = 10)
