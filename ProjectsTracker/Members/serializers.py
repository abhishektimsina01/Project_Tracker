from rest_framework import serializers
from .models import Member
from Auth.serializers import CustomUserSerializer
from .models import Member

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

# this serializer contains all the base of our basemodel
class BaseSerializer(serializers.Serializer):
    pass

# this is for the model serializer
class MemberSerializer(BaseSerializer):

    member_id = serializers.UUIDField(required = False)
    name = serializers.CharField(required = False)
    availability = serializers.BooleanField(required = False)
    department = serializers.ChoiceField(choices= Member.Department.choices, required = True)
    role = serializers.ChoiceField(choices= Member.Role.choices, required = False)
    user_id = serializers.PrimaryKeyRelatedField(write_only = True, queryset =CustomUser.objects.all())
    created_at = serializers.DateTimeField(read_only = True)

    def create(self, validated_data):
        print("to be created member data")
        print(validated_data)
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # make changes here not now
        instance.save()
        return instance


# this is for the member with the user populated
class MemberUserSerializer(MemberSerializer):
    user = CustomUserSerializer(source = "user_id", read_only = True)


# this is for the lead model
class LeadSerializer(BaseSerializer):
    pass


# this is for the project manager model
class ProjectManagerSerializer(BaseSerializer):
    pass