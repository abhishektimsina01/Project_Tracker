from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer, MyTokenRefreshSerializer
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.db import IntegrityError
CustomUser = get_user_model()

# Create your views here.
@api_view(['POST'])
def regsiter(request):
    print(request.data)
    # serializer
    serializer = CustomUserSerializer(data = request.data)
    if not serializer.is_valid():
        print("error")
        return Response(serializer.errors)
    print(serializer.validated_data)
    try:    
        user = serializer.save()
    except IntegrityError as e:
        return Response({
            "error_message" : "user already exist",
            # "error" : IntegrityError
        })
    print(type(user))
    refresh = RefreshToken.for_user(user)
    access = str(refresh.access_token)
    refresh = str(refresh)
    response = Response(serializer.data)
    response.set_cookie(
        key = "access",
        value=access,
        httponly=True,
        secure=True,
        max_age=60*10
    )
    response.set_cookie(
        key = "refresh",
        value=refresh,
        httponly=True,  
        secure=True,
        max_age=60*60*24
    )
    return response
    

class LogIn(TokenObtainPairView):
    # we can use the post method of this built-in view
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        print(request.data)
        response = super().post(request, *args, **kwargs)
        access = response.data.get("access")
        refresh = response.data.get("refresh")
        response.set_cookie(
            key = "access",
            value=access,
            httponly=True,
            secure=True,
            max_age=60*10
        )
        response.set_cookie(
            key = "refresh",
            value= refresh,
            httponly=True,  
            secure=True,
            max_age=60*60*24
        )
        response.data.pop("access")
        response.data.pop("refresh")
        return response


class Refresh(APIView):
    def get(self, request : Request):
        # accessig the refresh token from the cookies
        refresh = request.COOKIES.get("refresh")
        print("before refresh")
        print(refresh)
        data = {
            "refresh" : refresh
        }
        serializer = MyTokenRefreshSerializer(data = data)
        if serializer.is_valid():
            data = serializer.validated_data
            access = data.get("access")
            refresh = data.get("refresh")
            response = Response({
                "message" : "token refreshed"
            })
            response.set_cookie(
                key = "access",
                value=access,
                httponly=True,
                secure=True,
                max_age=60*10
            )
            response.set_cookie(
                key = "refresh",
                value= refresh,
                httponly=True,  
                secure=True,
                max_age=60*60*24
            )
            return response
        return Response(serializer.errors)


class LogOut(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        refresh = request.COOKIES.get("refresh")
        data = {
            "refresh" : refresh
        }
        serializer = TokenBlacklistSerializer(data = data)
        if serializer.is_valid():
            data = serializer.validated_data
            response = Response({
                "message" : "LoggedOut"
            })  
            response.delete_cookie("access")
            response.delete_cookie("refresh")
            return response
        return Response(serializer.errors)


@api_view(['DELETE'])
def deleteAllUser(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many = True)
    print(serializer.data)
    users.delete()
    return Response(serializer.data)