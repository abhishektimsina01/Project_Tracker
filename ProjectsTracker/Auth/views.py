from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView, TokenRefreshView
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
CustomUser = get_user_model()

# Create your views here.
@api_view(['POST'])
def regsiter(request):
    print(request.data)
    return Response(request.data)


class LogIn(TokenObtainPairView):
    # we can use the post method of this built-in view
    def post(self, request, *args, **kwargs):
        # logics
        # return super().post(request, *args, **kwargs)
        pass


class Refresh(TokenRefreshView):
    def get(self, request):
        pass


class LogOut(TokenBlacklistView):
    def get(self, request):
        pass