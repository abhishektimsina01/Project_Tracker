from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

CustomModel = get_user_model()

# ensure that the user is the employee so that we can use his/her id to access datas
class IsMember(BasePermission):
    def has_permission(self, request, view):
        # we get the user data after the authentiction is done
        print(request.user.is_authenticated)
        user_data = request.user
        print(user_data)
        if user_data.roles == CustomModel.Role.MEMBER:
            # the user has the permission
            print("the user has the permission so we are going to move forward")
            return True
        else:
            print("the user does not has the permission")
            return False

class IsPM(BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        user_data = request.user
        if user_data.roles == CustomModel.Role.PM:
            print("the user has the permission so we are going to move forward")
            return True
        else:
            print("the user does not have the permission")
            return False