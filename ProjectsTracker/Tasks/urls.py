from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import createTask, getTasks, getTask, changeState, TasksViewSet


router = DefaultRouter()
# router.register("tasks", TasksViewSet.as_view(), basename="tasks")

urlpatterns = [
    path("createTask/", createTask),
    path("getTasks/", getTasks),
    path("getTask/<uuid:task_id>", getTask),
    path("changeState/<uuid:task_id>", changeState)
]
