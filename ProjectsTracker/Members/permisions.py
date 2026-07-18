from rest_framework.permissions import BasePermission

# ensure that the user is the employee so that we can use his/her id to access datas
class IsMember(BasePermission):
    pass