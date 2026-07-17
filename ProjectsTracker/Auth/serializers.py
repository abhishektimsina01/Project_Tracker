from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, TokenBlacklistSerializer

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

class CustomUserSerializer(serializers.Serializer):
        
    id = serializers.UUIDField(read_only = True)
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)
    email = serializers.CharField(required = True)
    roles = serializers.CharField(required = False)
    gender = serializers.CharField(required = False)
    created_at = serializers.DateTimeField(read_only = True)

    # creating the user of the class CustomUser needs the create_user
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    # we have to get the data from the validated_data and set to instance
    # instance is already the object of CustomUser model so we can use .save()
    def update(self, instance, validated_data):
        
        instance.save()
        return 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        return super().get_token(user)
    
    def validate(self, attrs):
        print("ya aayo")
        data = super().validate(attrs)
        data["user"] = {
            "id" : self.user.id,
            "username" : self.user.username
        }
        print(data)
        return data

# it can be avoided by directly using the TokenRefreshSerializer too
class MyTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        return super().validate(attrs)