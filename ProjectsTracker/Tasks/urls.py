from django.urls import path
from .views import createTask, getTasks

urlpatterns = [
    path("createTask/", createTask),
    path("getTasks/", getTasks)
]