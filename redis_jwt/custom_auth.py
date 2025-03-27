from typing import Optional
from django.utils.cache import caches
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication, AuthUser
from rest_framework_simplejwt.tokens import Token


class CustomJWTAuth(JWTAuthentication):
    def authenticate(self, request: Request) -> Optional[tuple[AuthUser, Token]]:
        authenticate_info = super().authenticate(request)
        if authenticate_info is None:
            return None
        user, token = authenticate_info
        check_in_blacklist = caches['blacklist'].get(str(token), False)
        if check_in_blacklist:
            return None
        check_in_whitelist = caches['whitelist'].get(str(token), False)
        if not check_in_whitelist:
            return None
        return user, token
