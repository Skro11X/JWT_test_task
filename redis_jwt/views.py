from django.core.cache import caches
from django.contrib.auth import authenticate,get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from redis_jwt.serializers import LoginSerializer


whitelist = caches["whitelist"]
blacklist = caches["blacklist"]


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user:
            token = AccessToken.for_user(user)
            whitelist.set(token, user.username, 600)
            return Response({'token': str(token)})
        else:
            return Response({"error": "Incorrect login or password."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        authorization = request.headers.get('Authorization', None)
        token = authorization.split()[1]
        username = whitelist.get(token, None)
        if username:
            whitelist.delete(token)
            blacklist.set(username, token, timeout=3600)
            return Response({"OK": f"{username} you are logaut, token in blacklist"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "token not found"}, status=status.HTTP_400_BAD_REQUEST)

