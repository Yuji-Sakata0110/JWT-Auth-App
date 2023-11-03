from django.urls import path, URLResolver
from .views import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
    TaskListCreateView,
    TaskDetailView,
)

urlpatterns: list[URLResolver] = [
    path(
        "api/token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"
    ),
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
