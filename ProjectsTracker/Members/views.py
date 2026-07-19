from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime, timedelta
# from .models import Member

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your views here.

#get own profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOwnProfile(request):
    request.method
    print(request.user.id)
    print(request.user.username)
    print(request.user.roles)
    return Response({
        "data" : request.method
    })


# check for the task assigned
@api_view(['GET'])
@permission_classes([])
def assignedTask(request):
    # all the assigned task to the employee
    pass


#
@api_view(['GET'])
@permission_classes([])
def projectsInvolvedIn(request):
    # all the projects that the user was on...
    # its hisotory
    # streaks
    pass