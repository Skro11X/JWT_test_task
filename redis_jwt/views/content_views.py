from django.core.cache import caches
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from redis_jwt.serializers import LoginSerializer
from redis_jwt.models import ExampleContent
from redis_jwt.views.token_logic import get_token_from_request


whitelist = caches['whitelist']
blacklist = caches['blacklist']


class RoleModelFieldContent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        token = get_token_from_request(request)
        username = whitelist.get(token, None)
        User = get_user_model()
        user = User.objects.get(username=username)
        content = get_object_or_404(ExampleContent, id=kwargs["id"])
        response_dict = {"content_for_both_roles": content.content_for_both_roles}
        if user.has_perm("redis_jwt.get_special_content"):
            response_dict["content_for_one_role"] = content.content_for_one_role
        return Response(response_dict)
