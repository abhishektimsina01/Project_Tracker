from django.urls import path
from .views import getOwnProfile

urlpatterns = [
    path("getOwnProfile/", getOwnProfile)
]
