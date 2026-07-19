from django.db import models
from uuid import uuid4

# Create your models here.
class TeamsModel(models.Model):
    
    team_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20)
    main_field_of_work = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)