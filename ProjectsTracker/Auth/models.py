from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):

    GENDER_ROLES = [
        ("male", "MALE"),
        ("female", "FEMALE"),
        ("other", "OTHER")
    ]
    ROLES = [
        ("member", "MEMBER"),
        ("lead", "LEAD"),
        ("pm", "PM")
    ]
    id = models.UUIDField(primary_key = True, default = uuid.uuid4) 
    gender = models.CharField(null= True, choices = GENDER_ROLES)
    roles = models.CharField(default="member", choices=ROLES)
    created_at = models.DateTimeField(auto_now = True)
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []