from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Member
from .serializers import MemberSerializer, MemberUserSerializer
from Auth.serializers import CustomUserSerializer
from .permisions import IsMember, IsPM
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your views here.

# create the employee
# to create the employee, the user should be the pm
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsPM])
def createMember(request):
    print(request.data)
    serializer = MemberSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)
    serializer.save()
    print(serializer.data)
    return Response(serializer.data)


#get own profile
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsMember])
def getOwnProfile(request):
    try:
        user = Member.objects.get(user_id = request.user.id)
    except Member.DoesNotExist:
        return Response({
            "error" : "User is not the member yet"
        })
    serializer = MemberUserSerializer(user)
    required_fields = ["id", "username", "roles"]
    items = list(serializer.data["user"].keys())
    if serializer.data.get("user"):
        for key in items:
            if key not in required_fields and key in serializer.data["user"]:
                serializer.data["user"].pop(key)
    return Response(serializer.data)


#
@api_view(['GET'])
@permission_classes([])
def projectsInvolvedIn(request):
    # all the projects that the user was on...
    # its hisotory
    # streaks
    pass