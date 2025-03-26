from django.core.cache import caches
from django.contrib.auth import authenticate,get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
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
            user = authenticate(username=username, password=password)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if user:
            token = AccessToken.for_user(user)
            whitelist.set(token, user.username, 600)
            return Response({'token': str(token)})
        else:
            user = get_user_model()
            user = user.objects.first()
            user.check_password()
            return Response({"error": "Incorrect login or password."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request):
        token = request.data.get('token', None)
        username = whitelist.get(token, None)
        if username:
            whitelist.delete(token)
            blacklist.set(username, token, timeout=3600)
            return Response({"OK": f"{token.username} you are logaut, token in blacklist"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
