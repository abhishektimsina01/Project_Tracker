from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"

    class Role(models.TextChoices):
        MEMBER =  "MEMBER", "Member"
        LEAD = "LEAD", "Lead"
        PM = "PM", "pm"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4) 
    gender = models.CharField(
        max_length=10,
        choices = Gender.choices)
    roles = models.CharField(
        max_length=10,
        default= Role.MEMBER,
        choices=Role.choices)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []