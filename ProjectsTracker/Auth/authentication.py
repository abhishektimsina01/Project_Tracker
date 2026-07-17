from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        print("AUTHENTICATION IS GOING ON")
        access_token = request.COOKIES.get("access")
        if access_token == None:
            # ends with None
            return None
        print(access_token)
        # validated_token = self.get_validated_token(access_token)
        try:
            validated_token = self.get_validated_token(access_token)
        except Exception as e:
            print(e.detail["messages"])
            raise InvalidToken({
                "details" : e.detail["messages"],
                "error" : 'Token has expired'
            })
        try:
            user = self.get_user(validated_token)
        except Exception as e:
            print(type(e))
            print("Auth error aayo")
            if isinstance(e, AuthenticationFailed):
                raise AuthenticationFailed({
                    "detial" : e.detail,
                    "error" : "user deos not exist"
                })
            
            if isinstance(e, InvalidToken):
                raise InvalidToken({
                    "error" : "Token contained no recognizable user identification"
                })
        print("AUTHENTICATION COMPLETED")
        return user, validated_token   