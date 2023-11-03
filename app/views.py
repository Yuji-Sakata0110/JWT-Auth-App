from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(responses={HTTP_200_OK: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(responses={HTTP_200_OK: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class TaskListCreateView(ListCreateAPIView):
    # debug=Trueの場合は、認証をはずす。
    permission_classes: tuple[type[AllowAny]] | tuple[type[IsAdminUser]] = (
        (AllowAny,) if settings.DEBUG else (IsAdminUser,)
    )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    # debug=Trueの場合は、認証をはずす。
    permission_classes: tuple[type[AllowAny]] | tuple[type[IsAdminUser]] = (
        (AllowAny,) if settings.DEBUG else (IsAdminUser,)
    )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
