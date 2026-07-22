from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from Members.permisions import IsLead, IsMember, IsPM
from .models import TaskModel
from .serializers import BasicTaskSerializer, AssignedByAndToContainedTask, MemberTaskSerializer
from Auth.serializers import CustomUserSerializer
from Members.models import Member
from Members.serializers import MemberSerializer
from django.contrib.auth import get_user_model
from django.utils import timezone

CustomUser = get_user_model()

# Create your views here.

# create the task
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createTask(request):    
    print(request.GET)
    try:
        print(request.data)
        serializer = AssignedByAndToContainedTask(data = request.data)
        print(serializer.is_valid())
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data)
    except Exception as e:
        print("error aayexa hai")
        if isinstance(e, ValidationError):
            print(e.detail)
            raise ValidationError({
                "details" : e.detail
            })

# get all the tasks
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsMember | IsLead | IsPM])
def getTasks(request):
    # role based authorization of the content
    # member
    if request.user.roles == CustomUser.Role.MEMBER:
        # i want my own tasks only
        print(request.user.roles)
        user = request.user
        member = user.member
        # with the help of the user.member we can perform the revrse relation
        print(type(member))
        print(member.member_id)
        customUser = CustomUserSerializer(request.user)
        print(customUser.data)
        # we will fetch the tasks assigned to the user
        # as we get multiple members from the fetch and thri task model objects attached to the assignedToTask
        member_tasks = Member.objects.prefetch_related("assignedToTask")
        print(len(member_tasks))
        print(member_tasks)
        # assigned_task = member_tasks.assignedToTask.all()
        # taskSerializer = BasicTaskSerializer(assigned_task, many = True)
        # memberSerializer = MemberSerializer(member_tasks)
        return Response({
            "data" : "data aauunu parney ho"
            # "task" : taskSerializer.data
            # "tasks" : tasksSerializer.data,
            # "taks_with_members" : memberTasksSerializer.data
        })

    # Lead
    elif request.user.roles == CustomUser.Role.LEAD:
        return Response({
            "message" : "you are a member"
        })

    # ProjectManager
    else:
        return Response({
            "message" : "you are a member"
        })