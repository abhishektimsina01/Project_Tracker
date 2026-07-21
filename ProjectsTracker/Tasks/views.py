from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Members.permisions import IsLead, IsMember, IsPM
from .models import TaskModel
from Members.models import Member
from django.contrib.auth import get_user_model
from django.utils import timezone

CustomUser = get_user_model()

# Create your views here.


# create the task
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsLead | IsPM])
def createTask(request):
    print(request.GET)
    


# get all the tasks
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsMember | IsLead | IsPM])
def getTasks(request):
    # use the same view for
    # multiple roles and state of the task
    pass