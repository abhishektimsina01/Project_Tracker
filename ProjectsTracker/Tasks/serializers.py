from rest_framework import serializers
from .models import TaskModel
from Members.models import Member
from Members.serializers import MemberSerializer

# making the basic serializer
class BasicTaskSerializer(serializers.Serializer):

    task_id = serializers.UUIDField(read_only = True)
    name = serializers.CharField(required = True)
    description = serializers.CharField(required  = False)
    state = serializers.ChoiceField(choices=TaskModel.STATE.choices, required = False)
    assigned_to = serializers.PrimaryKeyRelatedField(write_only = True, queryset = Member.objects.all())
    assigned_by = serializers.PrimaryKeyRelatedField(write_only = True, queryset = Member.objects.all())
    # project_id = serializers.PrimaryKeyRelatedField(write_only = True, queryset = Projects.objects.all())
    deadline = serializers.DateTimeField(required = False)
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    def create(self, validated_data):
        print("**validated task data")
        # logic to add if i just want to do something with the data before the creation
        return TaskModel.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.save()
        return instance


# if the data of the assigned by and to member data required then used
class AssignedByAndToContainedTask(BasicTaskSerializer):
    assigned_to_data = MemberSerializer(source = "assigned_to", read_only = True)
    assigned_by_data = MemberSerializer(source = "assigned_by", read_only = True)
