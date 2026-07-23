from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from Members.permisions import IsLead, IsMember, IsPM
from .models import TaskModel
from .serializers import BasicTaskSerializer, AssignedByAndToContainedTask, AssignedByContainedTask, AssignedToContainedTask
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
        # for only the member
        member_tasks = Member.objects.prefetch_related("assignedToTask").get(member_id = member.member_id)
        print("type", type(member_tasks))
        print(member_tasks)
        assigned_task = member_tasks.assignedToTask.all()
        print("type", type(assigned_task))
        print(assigned_task)
        for task in assigned_task:
            print(type(task.assigned_to))
        taskSerializer = BasicTaskSerializer(assigned_task, many = True)
        return Response({
            "tasks" : taskSerializer.data
        })

    
    elif request.user.roles == CustomUser.Role.LEAD:
        # we get the data ofthe user who is the Lead for now
        user = request.user
        # get the member from the user with the reverse relation
        member = user.member
        # passing the member to the member serializer
        member_data = MemberSerializer(member)
        print(member_data.data)
        # prefetch the member with all the tasks which have the assignedBy id as the member id
        # it first of all performs the select query to get the member with that id
        # then, select all the tasks where, the FK having the related_name assignedByTask are in the list of all the member_ids fetched till now
        members_with_tasks = Member.objects.prefetch_related("assignedByTask").get(member_id = member.member_id)
        all_assigned_tasks = members_with_tasks.assignedByTask.all()
        # then it creates a dictionary where each member id is keyed for list of task objects fetched
        serializedTasks = BasicTaskSerializer(all_assigned_tasks, many = True)
        print(serializedTasks.data)
        # now select all the tasks from the
        return Response({
            "my_data" : member_data.data,
            "tasks" : serializedTasks.data
        })

    # ProjectManager
    else:
        # we need to find all the tasks that the all the leads has made till now
        # project manager
        # since the user is not directly associated with the task being the project manager,
        # we need to have the project - task - project manager relation
        user = request.user
        print(user.id)
        return Response({
            "message" : "you are a member"
        })


# for now, no project manager, can be added later
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsMember | IsLead])
def getTask(request, task_id):
    # what we have to do here is, whetehr the role of the user authorizes the user to have that access or not
    # if member then no access, if the user is lead then he/she can get the access
    # we need to fetch the specific task that the user wants
    print(task_id)
    print(request.user)
    member = request.user.member
    print(type(member))
    if request.user.roles == CustomUser.Role.LEAD:
        # see if the tasks belongs to the member or not
        try:
            task = TaskModel.objects.get(assigned_to = member.member_id)
        except TaskModel.DoesNotExist:
            return Response({
                "error" : "u cannot view the task u did not got"
            })
    else:
        task = TaskModel.objects.get(task_id = task_id)
        print(task.assigned_by_id)
        taskSerializer = AssignedToContainedTask(task)
        return Response(taskSerializer.data)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changeState(request, task_id):
    # we need to check the role of the user who tried to do the changes
    print(request.user)


class TasksViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        pass

    def retrieve(self, request):
        pass

    def destroy(self, reuqest):
        pass

    def update(self, request):
        pass

    def partial_update(self, request):
        pass

    def create(self, requet):
        pass