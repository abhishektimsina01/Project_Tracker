from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    # how is the data stored in our CustomUserModel
    def create_user(self, username, password = None, email = None, **extra_fields):
        # username, password, email are required we check if it was sent
        # all the extra fields are inside the **extra_fields packed
        if not username or not password or not email:
            print("username field was not sent")
            raise ValueError("one of the important credentials was not given")
        # after we validate all were given, we create the CustomUser object
        user = self.model(
            username = username,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        # save in the CustomUser model
        user.save(using = self._db)
        print(user)
        return user
    
    
    def create_superuser(self, username, password = None, email = None, **extra_fields):
        # we have to ensure that the certain properties are true for the user to be superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("user must be a staff")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("user must be superuser")
        
        # after all the checking we pass it to create_user() for flexibility
        return self.create_user(
            username= username,
            password= password,
            email=email,
            **extra_fields
        )