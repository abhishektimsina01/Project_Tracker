from django.urls import path
from .views import getOwnProfile, createMember

urlpatterns = [
    path("createMember/", createMember),
    path("getOwnProfile/", getOwnProfile)
]
