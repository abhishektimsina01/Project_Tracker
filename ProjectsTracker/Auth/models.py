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
    user_id = models.UUIDField(primary_key = True, default = uuid.uuid4) 
    gender = models.CharField(null= False, choices = GENDER_ROLES)
    is_employee = models.BooleanField(default=True, null= False)
    is_lead = models.BooleanField(default = False, null = False)
    is_project_manager = models.BooleanField(default = False, null = False)
    roles = models.CharField(default="member", choices=ROLES)
    created_at = models.DateTimeField(auto_now = True)
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    @property
    def who_am_i(self):
        if self.is_employee:
            return "employee"
        elif self.is_lead:
            return "lead"
        else:
            return "project_manager"