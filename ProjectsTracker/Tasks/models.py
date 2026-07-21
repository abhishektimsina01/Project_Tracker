from django.db import models
from uuid import uuid4
from Members.models import Member
# , Lead, ProjectManager
# from Projects.models import ProjectModel
from django.utils import timezone
from datetime import timedelta

def default_deadline_time():
    return timezone.now() + timedelta(days=1)

# Create your models here.
class TaskModel(models.Model):

    class STATE(models.TextChoices):
        ASSIGNED = "ASSIGNED", "ASSIGNED"
        STARTED = "STARTED", "STARTED"
        IN_PROGRESS = "IN_PROGRESS", "IN_PROGRESS"
        COMPLETED = "COMPLETED", "COMPLETED"
        CHECK = "CHECKING", "CHECKING"

    task_id = models.UUIDField(primary_key=True, default= uuid4)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150, null=True)
    state = models.CharField(max_length=11, default = STATE.ASSIGNED, choices = STATE.choices)
    assigned_to = models.ForeignKey(
        Member,
        on_delete = models.CASCADE,
        related_name = "assignedToTask"
    )
    assigned_by = models.ForeignKey(
        Member,
        on_delete= models.CASCADE,
        related_name= "assignedByTask"
    )
    # project_id = models.ForeignKey(
    #     ProjectModel,
    #     on_delete=models.CASCADE,
    #     related_name= "tasks"
    # )
    deadline = models.DateTimeField(default = default_deadline_time)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)