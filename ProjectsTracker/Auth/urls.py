from django.urls import path
from .views import LogIn, LogOut, Refresh, regsiter, deleteAllUser

urlpatterns = [
    path("login/",LogIn.as_view()),
    path("register/", regsiter),
    path("refresh/", Refresh.as_view()),
    path("logout/", LogOut.as_view()),
    path("deleteAllUser/", deleteAllUser)
]
