from django.urls import path
from redis_jwt.views import LoginView, LogoutView, RoleModelFieldContent


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('content/<int:id>/', RoleModelFieldContent.as_view())
]