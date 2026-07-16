from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView, TokenRefreshView
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

# Create your views here.