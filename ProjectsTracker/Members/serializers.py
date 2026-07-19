from rest_framework import serializers
from .models import Member
from Auth.serializers import CustomUserSerializer
from .models import Member

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

class MemberSerializer(serializers.Serializer):

    member_id = serializers.UUIDField(required = False)
    name = serializers.CharField(required = False)
    availability = serializers.BooleanField(required = False)
    department = serializers.ChoiceField(choices= Member.Department.choices, required = True)
    role = serializers.ChoiceField(choices= Member.Role.choices, required = False)
    user_id = serializers.PrimaryKeyRelatedField(write_only = True, queryset =CustomUser.objects.all())
    user = CustomUserSerializer(source = "user_id", read_only = True)
    created_at = serializers.DateTimeField(read_only = True)

    def create(self, validated_data):
        print("to be created member data")
        print(validated_data)
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # make changes here not now
        instance.save()
        return instance