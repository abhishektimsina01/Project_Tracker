from django.db import models
import uuid
from django.conf import settings

# Create your models here.
# we need to create the employee model for the data of the employee and 
# connection to the team model (many to one)
# connection to the project (many to one) as one employee can get associalted to only one project at a time


# this is the abstract model, which contains fields, properties and methods that the multiple models can inherit
class AbstractRoleModel(models.Model):
    class Role(models.TextChoices):
        INTERN = "intern","INTERN"
        JUNIOR = "junior", "JUNIOR"
        SENIOR = "senior", "SENIOR"

    class Department(models.TextChoices):
        BACKEND = "backend", "BACKEND"
        FRONTEND = "frontend", "FRONTEND"
        QA = "QA", "QA"
        TESTER = "tester", "TESTER"
        AI = "AI", "AI"
        PM = "PM", "PM"

    name = models.CharField(max_length=20)
    availability = models.BooleanField(default= False)
    department = models.CharField(choices = Department.choices)
    role = models.CharField(choices = Role.choices, default = Role.INTERN)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Member(AbstractRoleModel):

    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="member")

    # team = models.ForeignKey(
    #     on_delete=models.CASCADE,
    #     relared_name="members"
    # )


# class Lead(AbstractRoleModel):

#     lead_id = models.UUIDField(primary_key=True, default = uuid.uuid4)


# # it has the M : M relation with the project as mutliple pm can get involved with multiple projects
# # M : M relation with the team as the same reason
# class ProjectManager(AbstractRoleModel):

#     pm_id = models.UUIDField(primary_key=True, default=uuid.uuid4)